# Name of the Knowledge Graph
**Authors:** Antrea Christou, Erin Rogers, Sydney Woods

## Use Case Scenario
### Narrative 
Adapted from `use-case.md`.

### Competency Questions
Adapted from `use-case.md`.

### Integrated Datasets
Adapted from `use-case.md`.

### References
Adapted from `use-case.md`.

## Modules
<!-- There should be one module section per module (essentially per key-notion) -->
### CrashType
**Source Pattern:** name of adapted source pattern
**Source Data:** name(s) of dataset(s) which populate this module

#### Description
Description Text (adapted from the rationale in `key-notions.md`).

![CrashType Schema Diagram](../schema-diagrams/CrashType.png)

### Axioms
* `CrashType SubClass Of Crash` <br />
Crash Types are part of the Crash Entity.
* `isCrashofType exactly 1 CrashType` <br />
There is only one Crash Type each time.
* `OccuredOnDate exactly 1 TemporalEntity` <br />
Each Crash Type occurs only once.

## PlaneModel
**Source Pattern:** name of adapted source pattern
**Source Data:** name(s) of dataset(s) which populate this module

#### Description
Description Text (adapted from the rationale in `key-notions.md`).

![PlaneModel Schema Diagram](../schema-diagrams/PlaneModel.png)

### Axioms
* `PlaneModel SubClass Of Plane` <br />
Every Plane Model Belongs is part of the Plane Entity.
* `isPlaneModelType exactly 1 PlaneModel` <br />
A Plane Model is of only one Plane.

## Part
**Source Pattern:** name of adapted source pattern
**Source Data:** name(s) of dataset(s) which populate this module

#### Description
Description Text (adapted from the rationale in `key-notions.md`).
![Part Schema Diagram](../schema-diagrams/part.graphml)
![Part](../schema-diagrams/part_img.png "Part")

### Axioms
* `isPartModelType min 1 PartModel` <br />
Each Part has at least one PartModel. 

## PartModel
**Source Pattern:** name of adapted source pattern
**Source Data:** name(s) of dataset(s) which populate this module

#### Description
Description Text (adapted from the rationale in `key-notions.md`).
![PartModel Schema Diagram](../schema-diagrams/part_model.graphml)
![PartModel](../schema-diagrams/part_model_img.png "PartModel")
![PartModel Dates Schema Diagram](../schema-diagrams/start_end_dates.graphml)
![PartModel Dates](../schema-diagrams/start_end_dates_img.png "PartModel Dates")

### Axioms
* `EndDate max 1 TemporalEntity` <br />
Each PartModel has at most one EndDate.
* `hasIdentifier exactly 1 Identifier` <br />
Each PartModel has exactly one Identifier. 
* `StartDate exactly 1 TemporalEntity` <br />
Each PartModel has exactly one StartDate.


#### Any remarks re: usage

## The Overall Knowledge Graph
### Namespaces
* prefix: namespace
* prefix: namespace

### Schema Diagram
![schema-diagram](./schema-diagram.png)

### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

### Usage
Adapted from `validation.md`, i.e., the competency questions + SPARQL queries.
