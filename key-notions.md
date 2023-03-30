# Key Notions 

* CrashType : States the type of the crash (if any) of a given airplane. - Pattern : Aggregation [link here]( https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/aggregation)
 * - Database : [link here]([https://www.ntsb.gov/safety/data/Pages/Data_Stats.aspx](https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908?resource=download)
* Crash : States whether or not a given plane has crashed. - Pattern : Event [link here](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/event)
 * - Database : [link here]([https://www.ntsb.gov/safety/data/Pages/Data_Stats.aspx](https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908?resource=download)
* PlaneModel : States the model of the plane. - Pattern : Identifier [link here](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier)
 * - Database : [link here](https://database.diecastmodelaircraft.com)
* Plane : ID of an individual aircraft. - Pattern : Identifier [link here](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier)
 * - Database : [link here](http://www.csgnetwork.com/aviationtypeid.html)
* Part : Gives the general part type (for example an engine or a propeller).
* PartModel : States the specific model number / name or type of a given Part. - Pattern : Identifier [link here]( https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier) 
  * PartModel Datasets - https://www.aircraftspruce.com/menus/st/ac.html 
* Dates : 
  * Dates Pattern : Temporal Extent [link here]( https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/temporal-extent)
* endDate : The date that a given PartModel stopped being manufactured on (if no longer in production - for example, production would hopefully stop when a recall occurs). 0/0/0 if still being manufactured.  
* startDate : The date that the given PartModel first began being produced. 
* ManufacturingCompany : The company that manufactures the given PartModel, ReplacementPart, or PlaneModel.  Pattern: Identifier [link here]( https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier) 
*   - Database: https://www.back4app.com/database/back4app/aircraft-make-and-model-list)
* Recall : Formal recall for a specific PartModel on an airplane. Pattern: Aggregation [link here]( https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/aggregation) 
*   - Database: https://drs.faa.gov/browse/ADFRAWD/doctypeDetails
* ReplacementPart : Official replacement part specified in the recall. Pattern: Identifer [link here]( https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier)  
*   - Database: https://drs.faa.gov/browse/ADFRAWD/doctypeDetails
