# Axioms based on Schemas :

[All Schemas Link](https://github.com/cs7810-group3/group3Project/tree/main/schema-diagrams)

### AirworthinessDirective

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/AirworthinessDirective.png)

#### Axioms
* `isAirworthinessDirectiveFor min 1 Part` <br />
The Airworthiness Directive is for at least one Part.
* `hasDate exactly 1 TemporalEntity` <br />
The Airworthiness Directive is issued on one date.

### CrashType

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/CrashType.png)

#### Axioms
* `CrashType SubClass Of Plane` <br />
Crash Types are part of the Plane Entity.
* `hasCrashType exactly 1 CrashType` <br />
There is only one Crash Type each time.
* `OccuredOnDate exactly 1 TemporalEntity` <br />
Each Crash Type occurs only once.


### ManufacturingCompany

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/ManufacturingCompany.png)

#### Axioms
* `manufactures min 1 Part` <br />
A Manufacturing Company must manufacture at least one aircraft Part.

### Part

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/Part.png)

#### Axioms
* `isMadeBy min 1 ManufacturingCompany` <br />
At least one Manufacturing Company must have produced a specific Part, but there can be more than one manufacturer.
* `hasAirworthinessDirective min 0 AirworthinessDirective` <br />
Not all Parts have an AirworthinessDirective, but there is no maximum one Part may have.


### Plane

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/Plane.png)

#### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

### PlaneID

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/PlaneID.png)

#### Axioms
* `PlaneID SubClass Of Plane` <br />
Every PlaneID is part of the Plane Entity.
* `hasPlaneID exactly 1 PlaneID` <br />
Every Plane has exactly one PlaneID.

### PlaneModel

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/PlaneModel.png)

#### Axioms
* `EndDate max 1 TemporalEntity` <br />
Each PartModel has at most one EndDate.
* `hasIdentifier exactly 1 Identifier` <br />
Each PartModel has exactly one Identifier. 
* `StartDate exactly 1 TemporalEntity` <br />
Each PartModel has exactly one StartDate.
