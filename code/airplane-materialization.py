# -*- coding: utf-8 -*-
"""
@author: SydneyWoods
"""

##### Graph stuff
import rdflib
from rdflib import URIRef, Graph, Namespace, Literal
from rdflib import OWL, RDF, RDFS, XSD, TIME
# Prefixes
name_space = "http://stko-kwg.geog.ucsb.edu/"
pfs = {
"kwgr": Namespace(f"{name_space}lod/resource/"),
"kwg-ont": Namespace(f"{name_space}lod/ontology/"),
"geo": Namespace("http://www.opengis.net/ont/geosparql#"),
"geof": Namespace("http://www.opengis.net/def/function/geosparql/"),
"sf": Namespace("http://www.opengis.net/ont/sf#"),
"wd": Namespace("http://www.wikidata.org/entity/"),
"wdt": Namespace("http://www.wikidata.org/prop/direct/"),
"rdf": RDF,
"rdfs": RDFS,
"xsd": XSD,
"owl": OWL,
"time": TIME,
"dbo": Namespace("http://dbpedia.org/ontology/"),
"time": Namespace("http://www.w3.org/2006/time#"),
"ssn": Namespace("http://www.w3.org/ns/ssn/"),
"sosa": Namespace("http://www.w3.org/ns/sosa/"),
"cdt": Namespace("http://w3id.org/lindt/custom_datatypes#"),
"grair": Namespace("https://group3/GenericOntology/Airplanes")
}
# Initialization shortcut
def init_kg(prefixes=pfs):
    kg = Graph()
    for prefix in pfs:
        kg.bind(prefix, pfs[prefix])
    return kg
# rdf:type shortcut
a = pfs["rdf"]["type"]

# ObjectProperty

# EndDate
endDate = pfs["grair"]["EndDate"]
# hasCrashed
hasCrashed = pfs["grair"]["hasCrashed"]
# isCrashOfType
isCrashOfType = pfs["grair"]["isCrashOfType"]
# hasIdentifier
hasIdentifier = pfs["grair"]["hasIdentifier"]
# IdentifierAsText
identifierAsText = pfs["grair"]["IdentifierAsText"]
# hasOperationDates
hasOperationDates = pfs["grair"]["hasOperationDates"]
# ClosedDate
closedDate = pfs["grair"]["ClosedDate"]
# hasPlaneID
hasPlaneId = pfs["grair"]["hasPlaneID"]
# hasAirworthinessDirective
hasAirworthinessDirective = pfs["grair"]["hasAirworthinessDirective"]
# hasDate
hasDate = pfs["grair"]["hasDate"]
# isPart
isPart = pfs["grair"]["isPart"]
# isPlaneModelType
isPlaneModelType = pfs["grair"]["isPlaneModelType"]
# Manufactures
manufactures = pfs["grair"]["manufactures"]
# OccuredOnDate
occuredOnDate = pfs["grair"]["OccuredOnDate"]
# StartDate
startDate = pfs["grair"]["StartDate"]
# usedIn
usedIn = pfs["grair"]["usedIn"]
# uses
uses = pfs["grair"]["uses"]
# isMadeBy
isMadeBy = pfs["grair"]["isMadeBy"]
# hasAirworthinessDirective
hasAirworthinessDirective = pfs["grair"]["hasAirworthinessDirective"]
# asString
asString = pfs["grair"]["asString"]
# partAsString
partAsString = pfs["grair"]["partAsString"]
# isAirworthinessDirectiveFor
isAirworthinessDirectiveFor = pfs["grair"]["isAirworthinessDirectiveFor"]


hasCrashOfType = pfs["grair"]["hasCrashOfType"]
isPlaneModelType = pfs["grair"]["isPlaneModelType"]
hasPlaneID=pfs["grair"]["hasPlaneID"]
occuredOnDate=pfs["grair"]["occuredOnDate"]

g = init_kg()

# How to add
# g.add( (subject_node, predicate_node, object_node) )

# Add nodes

# Plane
g.add((pfs["grair"]["Plane"], isPlaneModelType, pfs["grair"]["PlaneModel"]))
g.add((pfs["grair"]["Plane"], uses, pfs["grair"]["Part"]))
g.add((pfs["grair"]["Plane"], hasPlaneId, pfs["grair"]["PlaneID"]))
# PlaneID
g.add((pfs["grair"]["PlaneID"], a, pfs["xsd"]["String"]))
# PlaneModel
g.add((pfs["grair"]["PlaneModel"], hasCrashed, pfs["grair"]["Crash"]))
# Crash
g.add((pfs["grair"]["Crash"], occuredOnDate, pfs["grair"]["TemporalEntity"]))
g.add((pfs["grair"]["Crash"], isCrashOfType, pfs["grair"]["CrashType"]))
g.add((pfs["grair"]["Crash"], a, pfs["xsd"]["String"]))
# Part
g.add((pfs["grair"]["Part"], partAsString, pfs["xsd"]["String"]))
g.add((pfs["grair"]["Part"], hasAirworthinessDirective, pfs["grair"]["AirworthinessDirective"]))
# AirworthinessDirective
g.add((pfs["grair"]["AirworthinessDirective"], isAirworthinessDirectiveFor, pfs["grair"]["Part"]))
g.add((pfs["grair"]["AirworthinessDirective"], hasDate, pfs["grair"]["TemportalEntity"]))
# ManufacturingCompany
g.add((pfs["grair"]["ManufacturingCompany"], manufactures, pfs["grair"]["Part"]))
g.add((pfs["grair"]["ManufacturingCompany"], asString, pfs["xsd"]["String"]))
# Part
g.add((pfs["grair"]["Part"], usedIn, pfs["grair"]["Plane"]))
g.add((pfs["grair"]["Part"], isMadeBy, pfs["grair"]["ManufacturingCompany"]))
g.add((pfs["grair"]["Part"], partAsString, pfs["xsd"]["String"]))


import pandas as pd

# Load the CSV file
engine_data = pd.read_excel('data_part_date_manufacturer_sydney.xlsx', header=0, index_col=None)
print("Part")
print(engine_data["Part"])

for index, row in engine_data.iterrows():
    part = row["Part"]
    manu = row["Manufacturer"]
    part_date = row["Date"]
    airworthiness = row["Airworthiness Directive"]
    
    eng_uri = URIRef(f"{name_space}lod/resource/Part{index}")
    manu_uri = URIRef(f"{name_space}lod/resource/ManufacuringCompany{index}")
    airworthiness_uri = URIRef(f"{name_space}lod/resource/AirworthinessDirective{index}")
    
    # Part
    g.add((eng_uri, a, pfs["grair"]["Part"]))
    g.add((eng_uri, partAsString, Literal(part)))
    g.add((eng_uri, hasAirworthinessDirective, airworthiness_uri))
    g.add((eng_uri, isMadeBy, manu_uri))
    g.add((eng_uri, partAsString, Literal(part)))
    # AirworthinessDirective
    g.add((airworthiness_uri, a, pfs["grair"]["AirworthinessDirective"]))
    g.add((airworthiness_uri, hasAirworthinessDirective, eng_uri))
    g.add((airworthiness_uri, hasDate, Literal(part_date)))
    g.add((airworthiness_uri, isAirworthinessDirectiveFor, eng_uri))
    # ManufacturingCompany
    g.add((manu_uri, a, pfs["grair"]["ManufacturingCompany"]))
    g.add((manu_uri, manufactures, eng_uri))
    g.add((manu_uri, asString, Literal(airworthiness)))
    
    
crash_data = pd.read_csv("Crashes.csv")
# Binary for crashtype : returns 1 if there is one or more fatalities in the crash.
crash_data['Fatalities'].mask(crash_data['Fatalities'] >=1 ,'1', inplace=True)
planeID=pd.read_csv("planeID.csv")
# Loop through the rows and create a new instance for each record
for index, row in crash_data.iterrows():
    plane_model = row["PlaneModel"]
    fatalities = row["Fatalities"]
    date=row["Date"]
    
    
    plane_uri = URIRef(f"{name_space}lod/resource/Plane{index}")
    g.add(( plane_uri, a, pfs["grair"]["Plane"]))
    g.add(( plane_uri, isPlaneModelType, Literal(plane_model)))
    crash_uri = URIRef(f"{name_space}lod/resource/CrashType{index}")
    g.add(( crash_uri, a, pfs["grair"]["CrashType"]))
    
    g.add((crash_uri, hasCrashOfType, Literal(fatalities)))
    g.add((crash_uri, occuredOnDate, Literal(date)))
    
for index, row in planeID.iterrows():
    planeID=row["PlaneID"]
    plane_uri = URIRef(f"{name_space}lod/resource/Plane{index}")
 
    

    g.add((plane_uri, hasPlaneID, Literal(planeID)))

    
   

output_file = "airplane_part_date_manufacturer_ttl_sydney.ttl"
temp = g.serialize(format="turtle", encoding="utf-8", destination=output_file)

