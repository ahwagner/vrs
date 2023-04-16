**Computational Definition**

A quantified set of :ref:`MolecularVariation` associated with a genomic locus.

**Information Model**

Some Genotype attributes are inherited from :ref:`Entity`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - id
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - The 'logical' identifier of the entity in the system of record, and MUST be represented as a CURIE. This 'id' is unique within a given system, but may also refer to an 'id' for the shared concept in  another system (represented by namespace, accordingly).
   *  - type
      - string
      - 1..1
      - MUST be "Genotype"
   *  - members
      - :ref:`GenotypeMember`
      - 1..m
      - Each GenotypeMember in `members` describes a :ref:`MolecularVariation` and the count of that variation at the locus.
   *  - count
      - :ref:`Number` | :ref:`IndefiniteRange` | :ref:`DefiniteRange`
      - 1..1
      - The total number of copies of all :ref:`MolecularVariation` at this locus, MUST be greater than or equal to the sum of :ref:`GenotypeMember` copy counts and MUST be greater than or equal to 1. If greater than the total of GenotypeMember counts, this field describes  additional :ref:`MolecularVariation` that exist but are not  explicitly described.
