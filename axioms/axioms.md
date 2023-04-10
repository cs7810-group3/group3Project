# Axioms based on Schemas :

[All Schemas Link](https://github.com/cs7810-group3/group3Project/tree/main/schema-diagrams)

## CrashType

 ![CrashType Schema Diagram](../schema-diagrams/CrashType.png)

### Axioms
* `CrashType SubClass Of Crash` <br />
Crash Types are part of the Crash Entity.
* `isCrashofType exactly 1 CrashType` <br />
There is only one Crash Type each time.
* `OccuredOnDate exactly 1 TemporalEntity` <br />
Each Crash Type occurs only once.


## CrashType

![Crash Schema Diagram](../schema-diagrams/CrashType.png)

### Axioms
* `isCrashofType exactly 1 CrashType` <br />
Every crash has exactly one Crash Type.
* `OccuredOnDate exactly 1 TemporalEntity` <br />
Every Crash has occured exactly once.

## PlaneModel

![PlaneModel Schema Diagram](../schema-diagrams/PlaneModel.png)

### Axioms
* `PlaneModel SubClass Of Plane` <br />
Every Plane Model Belongs is part of the Plane Entity.
* `isPlaneModelType exactly 1 PlaneModel` <br />
A Plane Model is of only one Plane.

## PlaneID

![PlaneID Schema Diagram](../schema-diagrams/PlaneID.png)


### Axioms
* `PlaneID SubClass Of Plane` <br />
Every PlaneID is part of the Plane Entity.
* `hasPlaneID exactly 1 PlaneID` <br />
Every Plane has exactly one PlaneID.



## Part
![Part Schema Diagram](../schema-diagrams/part.graphml)
![Part](../schema-diagrams/part_img.png "Part")
### Axioms
* `isPartModelType min 1 PartModel` <br />
Each Part has at least one PartModel. 

## PartModel
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

