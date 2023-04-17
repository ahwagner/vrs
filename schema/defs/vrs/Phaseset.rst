**Computational Definition**

A set of trans-phased Variation objects.

**Information Model**

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - type
      - string
      - 1..1
      - MUST be "Phaseset".
   *  - members
      - :ref:`MolecularVariation`
      - 2..m
      - Each object in `members` describes a :ref:`MolecularVariation` that is known to be in-Trans with the other members.
