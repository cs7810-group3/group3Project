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
"ex": Namespace("https://example.com/")
}
# Initialization shortcut
def init_kg(prefixes=pfs):
    kg = Graph()
    for prefix in pfs:
        kg.bind(prefix, pfs[prefix])
    return kg
# rdf:type shortcut
a = pfs["rdf"]["type"]

# isPlaneModelType
isPlaneModelType = pfs["ex"]["isPlaneModelType"]
# usedIn
usedIn = pfs["ex"]["usedIn"]
# uses
uses = pfs["ex"]["uses"]
# hasCrashed
hasCrashed = pfs["ex"]["hasCrashed"]
# isCrashOfType
isCrashOfType = pfs["ex"]["isCrashOfType"]
# hasCausedCrash
hasCausedCrash = pfs["ex"]["hasCausedCrash"]
# beganManufacturingOn
beganManufacturingOn = pfs["ex"]["beganManufacturingOn"]
# stoppedManufacturingOn
stoppedManufacturingOn = pfs["ex"]["stoppedManufacturingOn"]
# hasRecall
hasRecall = pfs["ex"]["hasRecall"]
# recalledOn
recalledOn = pfs["ex"]["recalledOn"]
# isPartModelType
isPartModelType = pfs["ex"]["isPartModelType"]
# madeBy
madeBy = pfs["ex"]["madeBy"]
# makesPart
makesPart = pfs["ex"]["makesPart"]
# shutDownServiceOn
shutDownServiceOn = pfs["ex"]["shutDownServiceOn"]

g = init_kg()

# How to add
# g.add( (subject_node, predicate_node, object_node) )

# Add a specific plane (individual)
g.add((pfs["ex"]["SR-71"], a, pfs["ex"]["Plane"]))
g.add((pfs["ex"]["SR-71"], a, pfs["ex"]["Military"]))

# Add nodes
# Plane 
g.add((pfs["ex"]["Plane"], uses, pfs["ex"]["Part"]))
g.add((pfs["ex"]["Part"], usedIn, pfs["ex"]["Plane"]))
g.add((pfs["ex"]["Military"], a, pfs["ex"]["Plane"]))
g.add((pfs["ex"]["Cargo"], a, pfs["ex"]["Plane"]))
g.add((pfs["ex"]["Passenger"], a, pfs["ex"]["Plane"]))
# PlaneModel
g.add((pfs["ex"]["Plane"], isPlaneModelType, pfs["ex"]["PlaneModel"]))
# Crash
g.add((pfs["ex"]["PlaneModel"], hasCrashed, pfs["ex"]["Crash"]))
g.add((pfs["ex"]["Crash"], isCrashOfType, pfs["ex"]["CrashType"]))
# PartModel
g.add((pfs["ex"]["PartModel"], hasCausedCrash, pfs["ex"]["Crash"]))
g.add((pfs["ex"]["PartModel"], beganManufacturingOn, pfs["ex"]["startDate"]))
g.add((pfs["ex"]["PartModel"], stoppedManufacturingOn, pfs["ex"]["endDate"]))
# Recall
g.add((pfs["ex"]["PartModel"], hasRecall, pfs["ex"]["Recall"]))
# recalledOnDate
g.add((pfs["ex"]["Recall"], recalledOn, pfs["ex"]["recalledOnDate"]))
# Part
g.add((pfs["ex"]["Part"], isPartModelType, pfs["ex"]["PartModel"]))
# ManufacturingCompany
g.add((pfs["ex"]["Part"], madeBy, pfs["ex"]["ManufacturingCompany"]))
g.add((pfs["ex"]["ManufacturingCompany"], makesPart, pfs["ex"]["Part"]))
# closedOnDate
g.add((pfs["ex"]["ManufacturingCompany"], shutDownServiceOn, pfs["ex"]["closedOnDate"]))


output_file = "airplane_output.ttl"
temp = g.serialize(format="turtle", encoding="utf-8", destination=output_file)





