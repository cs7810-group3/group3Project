# Name of the Knowledge Graph
**Authors:** Antrea Christou, Erin Rogers, Sydney Woods

## Use Case Scenario
### Narrative 

Some common goals include:<br>
	*	Improving data organization and management: A knowledge graph can help organize complex and interconnected data, making it easier to understand and manage.<br>
	*	Enabling effective search and retrieval of information: By organizing data in a structured way, a knowledge graph can make it easier to search for and retrieve relevant information.<br>
	*	Supporting data analysis and decision-making: A knowledge graph can help identify patterns, insights, and relationships that might not be visible in traditional data structures, enabling better decision-making.<br>
	*	Facilitating collaboration and communication: By providing a common framework for understanding data, a knowledge graph can facilitate collaboration and communication among teams.<br>

A knowledge graph can also help to streamline communication and collaboration among different stakeholders in the aviation industry, enabling them to make more informed decisions and take actions that improve the overall safety and efficiency of the industry.

In our knowledge graph, we aim to support aircraft owners, pilots, and maintainers. Their end goal is to keep aircraft flightworthy, which means frequent maintenance. Maintenance sometimes means sending parts out for repairs or even replacing them altogether, but a large percentage of aircraft used today is more than fifty years old and their manufacturer may have gone out of business or been subsumed by a competitor. It can be difficult to know what companies are supporting the maintenance for what models based upon service logs and possibly out of date owner’s manuals. Keeping aircraft flightworthy also involves knowing what issues a specific model may be prone to, such as brakes on Cessna 140s leading to the airplanes flipping over on the runway, and knowing when parts are recalled. Recalls can happen decades after an aircraft is no longer in production.<br>

Additionally, there could be potential use by businesses looking to see what companies are their biggest remaining competition in the manufacturing of parts. As previously stated, some manufacturers may have been merged together (a similar situation as has been seen with wireless providers in the USA in the early to mid 2010s).<br>
With the issue of manufacturers going out of business, another possible use would be for owners to see if there are any compatible parts still being made to replace or repair parts no longer being made. This functionality would also be useful should any parts be recalled to figure out what is the next best option to keep the aircraft in a safe condition for flying.<br>
By including details about the most common issues different models of the same parts are prone to, this could allow an individual to make a clear decision on what part they would use. For example if the owner of an aircraft has previously encountered a specific issue and knows how to fix it, they may pick the part that is known to have that issue over a part that they do not know how to fix the issues with. Or if the aircraft owner is looking to expand their knowledge on how to fix issues, they may opt to purchase the part they did not know how to fix and then learn to do so.    

### Competency Questions
* How would you query the knowledge graph to identify all airplane parts manufactured by a specific company?
* Show the top A most common plane models. (This would be the list on length A, of the planes with the highest count of total manufactured / made)  
* What times of year are associated with higher crash ratings that were fatal?
* How many parts each company makes?
* Show the unique plane ID's paired with their corresponding plane model type.
* Show the parts along with their manufactiring company and their airworthiness directive.

### Integrated Datasets
[Crash Types](https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908?resource=download)
[Plane Models](http://aviationdb.net/aviationdb/AircraftQuery#SUBMIT)
[Airworthiness Directives](https://drs.faa.gov/browse/ADFRAWD/doctypeDetails)


### References
* https://gama.aero/facts-and-statistics/statistical-databook-and-industry-outlook/annual-data/ - original access date: 2/16/2023<br>
* https://www.faa.gov/airports/engineering/aircraft_char_database - original access date: 02/16/2023<br>
* Specifically https://www.faa.gov/airports/engineering/aircraft_char_database/data - original access date: 02/16/2023<br>  
* https://www.faa.gov/data_research/aviation_data_statistics - original access date: 02/16/2023<br>
* https://ww2db.com/doc.php?q=399 - original access date: 02/16/2023<br>
* Might be more from the directory one level up found here https://ww2db.com/doc.php - original access date: 02/16/2023<br> 
* https://data.world/data-society/airplane-crashes -original access date: 02/16/2023<br> 
* https://data.world/sanfrancisco/u7dr-xm3v -original access date: 02/16/2023<br> 
* https://www.kaggle.com/code/jiaowoguanren/airplanes-motorbikes-schooners-tf-efficientnet/data -original access date: 02/16/2023<br> 
* https://industry.flightaware.com/ownersandoperators -original access date: 02/16/2023<br> 
* https://drs.faa.gov/browse/ADFRAWD/doctypeDetails -original access date: 03/18/2023<br>


## Modules
<!-- There should be one module section per module (essentially per key-notion) -->
### AirworthinessDirective
**Source Pattern:** [Aggregation]( https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/aggregation)
**Source Data:** [FAA Dynamic Regulatory System](https://drs.faa.gov/browse/ADFRAWD/doctypeDetails)

#### Description
Airworthiness Directives are Part recalls issued by the FAA.

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/AirworthinessDirective.png)

#### Axioms
* `isAirworthinessDirectiveFor min 1 Part` <br />
The Airworthiness Directive is for at least one Part.
* `hasDate exactly 1 TemporalEntity` <br />
The Airworthiness Directive is issued on one date.

#### Remarks
* Any remarks re: usage

### CrashType
**Source Pattern:** [Event](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/event)
**Source Data:** [Crashes Since 1908](https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908?resource=download)

#### Description
Binary value identifying if the Plane has had any fatal crashes.

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/CrashType.png)

#### Axioms
* `CrashType SubClass Of Plane` <br />
Crash Types are part of the Plane Entity.
* `hasCrashType exactly 1 CrashType` <br />
There is only one Crash Type each time.
* `OccuredOnDate exactly 1 TemporalEntity` <br />
Each Crash Type occurs only once.

#### Remarks
* Any remarks re: usage

### ManufacturingCompany
**Source Pattern:** [Identifier]( https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier) 
**Source Data:** [FAA Dynamic Regulatory System](https://drs.faa.gov/browse/ADFRAWD/doctypeDetails)
#### Description
Manufacturing Companies create Parts for aircraft.

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/ManufacturingCompany.png)

#### Axioms
* `manufactures min 1 Part` <br />
A Manufacturing Company must manufacture at least one aircraft Part.

#### Remarks
* Any remarks re: usage

### Part
**Source Pattern:** [Identifier]( https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier)
**Source Data:** [FAA Dynamic Regulatory System](https://drs.faa.gov/browse/ADFRAWD/doctypeDetails)

#### Description
Specific components of an airplane.

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/Part.png)

#### Axioms
* `isMadeBy min 1 ManufacturingCompany` <br />
At least one Manufacturing Company must have produced a specific Part, but there can be more than one manufacturer.
* `hasAirworthinessDirective min 0 AirworthinessDirective` <br />
Not all Parts have an AirworthinessDirective, but there is no maximum one Part may have.

#### Remarks
* Any remarks re: usage

### Plane
**Source Pattern:** name of adapted source pattern
**Source Data:** name(s) of dataset(s) which populate this module

#### Description
An individual Plane Entity.

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/Plane.png)

#### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

#### Remarks
* Any remarks re: usage

### PlaneID
**Source Pattern:** [Identifier]( https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier)
**Source Data:** [Aviation IDs](http://www.csgnetwork.com/aviationtypeid.html)

#### Description
Description Text (adapted from the rationale in `key-notions.md`).

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/PlaneID.png)

#### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

#### Remarks
* Any remarks re: usage

### PlaneModel
**Source Pattern:** [Identifier]( https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier)
**Source Data:** [FAA Dynamic Regulatory System](https://drs.faa.gov/browse/ADFRAWD/doctypeDetails)

#### Description
States the model of the Plane.

![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/PlaneModel.png)

#### Axioms

#### Remarks
* Any remarks re: usage

## The Overall Knowledge Graph
### Namespaces
* prefix: namespace
* prefix: namespace

### Schema Diagram
![./schema-diagram.png](https://github.com/cs7810-group3/group3Project/blob/main/schema-diagrams/schema_attempt_seven.png)

### Axioms
* `isAirworthinessDirectiveFor min 1 Part` <br />
The Airworthiness Directive is for at least one Part.
* `hasDate exactly 1 TemporalEntity` <br />
The Airworthiness Directive is issued on one date.
* `CrashType SubClass Of Plane` <br />
Crash Types are part of the Plane Entity.
* `hasCrashType exactly 1 CrashType` <br />
There is only one Crash Type each time.
* `OccuredOnDate exactly 1 TemporalEntity` <br />
Each Crash Type occurs only once.
* `manufactures min 1 Part` <br />
A Manufacturing Company must manufacture at least one aircraft Part.
* `isMadeBy min 1 ManufacturingCompany` <br />
At least one Manufacturing Company must have produced a specific Part, but there can be more than one manufacturer.
* `hasAirworthinessDirective min 0 AirworthinessDirective` <br />
Not all Parts have an AirworthinessDirective, but there is no maximum one Part may have.

### Usage
Adapted from `validation.md`, i.e., the competency questions + SPARQL queries.
