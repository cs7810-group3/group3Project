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
* How would you query the knowledge graph to identify all airplanes manufactured by a specific company?
* Show the top A most common planes. (This would be the list on length A, of the planes with the highest count of total manufactured / made)  
* Are their connections between aircraft models and specific crash types?
* What aircraft have had part recalls, and are there trends?
* What aircraft manufacturers support part production for older aircraft and are there aircraft with no manufacturer support?
* What part recalls are associated with the most crashes?

### Integrated Datasets
[Crash Types](https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908?resource=download)
[Plane Models](http://aviationdb.net/aviationdb/AircraftQuery#SUBMIT)
[Airworthiness Directives](https://drs.faa.gov/browse/ADFRAWD/doctypeDetails)


### References
Adapted from `use-case.md`.

## Modules
<!-- There should be one module section per module (essentially per key-notion) -->
### Module X
**Source Pattern:** name of adapted source pattern
**Source Data:** name(s) of dataset(s) which populate this module

#### Description
Description Text (adapted from the rationale in `key-notions.md`).

![schema-diagram](./schema-diagram.png)

#### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

#### Remarks
* Any remarks re: usage

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
