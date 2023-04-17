import json

import yaml
import python_jsonschema_objects as pjs
from schema.helpers import pjs_filter
from ga4gh.gks.metaschema.tools.source_proc import YamlSchemaProcessor
from jsonschema import validate, RefResolver
import pytest
from pygit2 import Repository
import re
from enum import Enum
import os

from config import vrs_json_path, vrs_yaml_path, root_dir

# Are the yaml and json parsable and do they match?
p = YamlSchemaProcessor(vrs_yaml_path)
j = json.load(open(vrs_json_path))


@pytest.mark.skip(reason='demo site, json match not required')
def test_json_yaml_match():
    assert p.for_js == j, "parsed yaml and json do not match"


# Can pjs handle this schema?
@pytest.mark.skip(reason='demo site, pjs parsing not required')
def test_pjs_smoke():
    ob = pjs.ObjectBuilder(pjs_filter(j))
    assert ob.build_classes()              # no exception => okay


@pytest.mark.skip(reason='demo site, validation testing not required')
def test_schema_validation():
    """Test that examples in validation/models.yaml are valid"""
    resolver = RefResolver.from_schema(j, store={"definitions": j})
    schema_definitions = j["definitions"]
    validation_models = root_dir / "validation" / "models.yaml"
    validation_tests = yaml.load(open(validation_models), Loader=yaml.SafeLoader)
    for cls, tests in validation_tests.items():
        for t in tests:
            validate(instance=t["in"],
                     schema=schema_definitions[cls],
                     resolver=resolver)

def test_maturity():
    """Test that all classes are at an appropriate maturity model for branch"""
    def assert_all_models_have_maturity_level(level):
        for cls in p.processed_classes:
            if not p.class_is_abstract(cls):
                cls_level = p.defs[cls].get('maturity', 'NA')
                try:
                    assert getattr(Maturity, cls_level).value >= getattr(Maturity, level).value
                except AssertionError:
                    msg = f'Maturity level for {cls} ({cls_level}) inappropriate for branch.'
                    print("\n" + msg)
                    assert cls_level == level, msg

    class Maturity(Enum):
        NA = 0
        Alpha = 1
        Beta = 2
        RC = 3
        Stable = 4

    target = os.getenv('github.base_ref', None)

    branch_name = target | Repository('.').head.shorthand
    if re.match('^\d+\.\d+$', branch_name):
        assert_all_models_have_maturity_level('Stable')
    elif re.match('^\d+\.\d+-beta$', branch_name):
        assert_all_models_have_maturity_level('Beta')
    elif re.match('^\d+\.\d+-rc$', branch_name):
        assert_all_models_have_maturity_level('RC')
    else:
        assert True
