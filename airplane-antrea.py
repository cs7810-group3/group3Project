# -*- coding: utf-8 -*-


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
"grair":Namespace("https://group3/GenericOntology/Airplanes/")
}

import pandas as pd

# Initialize the graph
g = Graph()
for prefix in pfs:
    g.bind(prefix, pfs[prefix])
a = pfs["rdf"]["type"]
isCrashOfType = pfs["grair"]["isCrashOfType"]
isPlaneModelType = pfs["grair"]["isPlaneModelType"]
hasPlaneID=pfs["grair"]["hasPlaneID"]
occuredOnDate=pfs["grair"]["occuredOnDate"]

# Load the CSV file
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
    g.add((plane_uri, a, pfs["grair"]["Plane"]))
    g.add((plane_uri, isPlaneModelType, Literal(plane_model)))
    g.add((plane_uri, isCrashOfType, Literal(fatalities)))
    g.add((plane_uri, occuredOnDate, Literal(date)))
    
for index, row in planeID.iterrows():
    planeID=row["PlaneID"]
    plane_uri = URIRef(f"{name_space}lod/resource/Plane{index}")

    g.add((plane_uri, hasPlaneID, Literal(planeID)))

# Serialize the graph to a file
g.serialize(destination='out.ttl', format='turtle')






