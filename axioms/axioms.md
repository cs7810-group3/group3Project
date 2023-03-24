# Axioms based on Schemas :

[All Schemas Link](https://github.com/cs7810-group3/group3Project/tree/main/schema-diagrams)

## Name of Module
* CrashType

### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

## Name of Module
* Crash

### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

## Name of Module
* PlaneModel

### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

## Name of Module
* Plane

### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

## Name of Module
* PlaneID

### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

## Part
![Part Schema Diagram](../schema-diagrams/part.graphml)
![Part](../schema-diagrams/part_img.png "Part")
### Axioms
* isPartModelType min 1 PartModel <br />
Each Part has at least one PartModel. 

## PartModel
![PartModel Schema Diagram](../schema-diagrams/part_model.graphml)
![PartModel](../schema-diagrams/part_model_img.png "PartModel")
![PartModel Dates Schema Diagram](../schema-diagrams/start_end_dates.graphml)
![PartModel Dates](../schema-diagrams/start_end_dates_img.png "PartModel Dates")

### Axioms
* EndDate max 1 TemporalExtent <br />
Each PartModel has at most one EndDate.
* hasIdentifier exactly 1 Identifier <br />
Each PartModel has exactly one Identifier. 
* StartDate exactly 1 TemporalExtent <br />
Each PartModel has exactly one StartDate.


