# Auto generated from chromo.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-07-09 12:32
# Schema: ChromoSchema
#
# id: https://w3id.org/biodatamodels/chromoschema
# description: Schema for representing Chromosomes and Chromosomal Regions. Objects created using this schema can
#              be directly worked with in YAML/Python, Additionally they can be translated to OWL
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CHR = CurieNamespace('CHR', 'http://purl.obolibrary.org/obo/CHR_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
CHROMOSCHEMA = CurieNamespace('chromoschema', 'https://w3id.org/biodatamodels/chromoschema/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EDAM = CurieNamespace('edam', 'http://edamontology.org/')
ENSEMBL = CurieNamespace('ensembl', 'http://identifiers.org/ensembl/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
GFF = CurieNamespace('gff', 'https://w3id.org/biodatamodels/gff/')
INSDC = CurieNamespace('insdc', 'http://identifiers.org/insdc/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
REFSEQ = CurieNamespace('refseq', 'http://identifiers.org/refseq/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CHROMOSCHEMA


# Types
class TaxonIdentifier(Uriorcurie):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "TaxonIdentifier"
    type_model_uri = CHROMOSCHEMA.TaxonIdentifier


class BandDescriptor(String):
    """ e.g. p, p1, p1.1, ... """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "BandDescriptor"
    type_model_uri = CHROMOSCHEMA.BandDescriptor


class ChromosomeNameType(String):
    """ E.g. chr1 """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ChromosomeNameType"
    type_model_uri = CHROMOSCHEMA.ChromosomeNameType


class StrandType(Integer):
    """ 0, 1, or -1 """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "StrandType"
    type_model_uri = CHROMOSCHEMA.StrandType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "LabelType"
    type_model_uri = CHROMOSCHEMA.LabelType


# Class references
class ChromosomePartId(extended_str):
    pass


class GenomeId(extended_str):
    pass


class GenomeBuildId(extended_str):
    pass


class OrganismTaxonId(extended_str):
    pass


@dataclass
class ChromosomePartCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHROMOSCHEMA.ChromosomePartCollection
    class_class_curie: ClassVar[str] = "chromoschema:ChromosomePartCollection"
    class_name: ClassVar[str] = "ChromosomePartCollection"
    class_model_uri: ClassVar[URIRef] = CHROMOSCHEMA.ChromosomePartCollection

    name: Optional[str] = None
    has: Optional[Union[Dict[Union[str, ChromosomePartId], Union[dict, "ChromosomePart"]], List[Union[dict, "ChromosomePart"]]]] = empty_dict()
    genomes: Optional[Union[Dict[Union[str, GenomeId], Union[dict, "Genome"]], List[Union[dict, "Genome"]]]] = empty_dict()
    taxons: Optional[Union[Dict[Union[str, OrganismTaxonId], Union[dict, "OrganismTaxon"]], List[Union[dict, "OrganismTaxon"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_dict(slot_name="has", slot_type=ChromosomePart, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="genomes", slot_type=Genome, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="taxons", slot_type=OrganismTaxon, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class ChromosomePart(YAMLRoot):
    """
    A Chromosome or a part of a chromosome (includes whole chromosomes, arms, and bands)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHROMOSCHEMA.ChromosomePart
    class_class_curie: ClassVar[str] = "chromoschema:ChromosomePart"
    class_name: ClassVar[str] = "ChromosomePart"
    class_model_uri: ClassVar[URIRef] = CHROMOSCHEMA.ChromosomePart

    id: Union[str, ChromosomePartId] = None
    band_descriptor: Optional[Union[str, BandDescriptor]] = None
    chromosome_name: Optional[Union[str, ChromosomeNameType]] = None
    build: Optional[Union[str, GenomeBuildId]] = None
    name: Optional[Union[str, LabelType]] = None
    type: Optional[Union[str, "EntityType"]] = None
    somal_type: Optional[Union[str, "AutosomeVsSexChromosome"]] = None
    sex_chromosome_type: Optional[Union[str, "SexChromosomeType"]] = None
    cell_location: Optional[Union[str, "LocationType"]] = None
    taxon: Optional[Union[str, TaxonIdentifier]] = None
    start: Optional[int] = None
    end: Optional[int] = None
    children: Optional[Union[Union[str, ChromosomePartId], List[Union[str, ChromosomePartId]]]] = empty_list()
    parent: Optional[Union[str, ChromosomePartId]] = None
    exact_mappings: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    exact_synonyms: Optional[Union[str, List[str]]] = empty_list()
    broad_synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChromosomePartId):
            self.id = ChromosomePartId(self.id)

        if self.band_descriptor is not None and not isinstance(self.band_descriptor, BandDescriptor):
            self.band_descriptor = BandDescriptor(self.band_descriptor)

        if self.chromosome_name is not None and not isinstance(self.chromosome_name, ChromosomeNameType):
            self.chromosome_name = ChromosomeNameType(self.chromosome_name)

        if self.build is not None and not isinstance(self.build, GenomeBuildId):
            self.build = GenomeBuildId(self.build)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.type is not None and not isinstance(self.type, EntityType):
            self.type = EntityType(self.type)

        if self.somal_type is not None and not isinstance(self.somal_type, AutosomeVsSexChromosome):
            self.somal_type = AutosomeVsSexChromosome(self.somal_type)

        if self.sex_chromosome_type is not None and not isinstance(self.sex_chromosome_type, SexChromosomeType):
            self.sex_chromosome_type = SexChromosomeType(self.sex_chromosome_type)

        if self.cell_location is not None and not isinstance(self.cell_location, LocationType):
            self.cell_location = LocationType(self.cell_location)

        if self.taxon is not None and not isinstance(self.taxon, TaxonIdentifier):
            self.taxon = TaxonIdentifier(self.taxon)

        if self.start is not None and not isinstance(self.start, int):
            self.start = int(self.start)

        if self.end is not None and not isinstance(self.end, int):
            self.end = int(self.end)

        if not isinstance(self.children, list):
            self.children = [self.children] if self.children is not None else []
        self.children = [v if isinstance(v, ChromosomePartId) else ChromosomePartId(v) for v in self.children]

        if self.parent is not None and not isinstance(self.parent, ChromosomePartId):
            self.parent = ChromosomePartId(self.parent)

        if not isinstance(self.exact_mappings, list):
            self.exact_mappings = [self.exact_mappings] if self.exact_mappings is not None else []
        self.exact_mappings = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.exact_mappings]

        if not isinstance(self.exact_synonyms, list):
            self.exact_synonyms = [self.exact_synonyms] if self.exact_synonyms is not None else []
        self.exact_synonyms = [v if isinstance(v, str) else str(v) for v in self.exact_synonyms]

        if not isinstance(self.broad_synonyms, list):
            self.broad_synonyms = [self.broad_synonyms] if self.broad_synonyms is not None else []
        self.broad_synonyms = [v if isinstance(v, str) else str(v) for v in self.broad_synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Genome(YAMLRoot):
    """
    Represents a sequenced genome, one per species.
    Each genome can be associated with one or more builds
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHROMOSCHEMA.Genome
    class_class_curie: ClassVar[str] = "chromoschema:Genome"
    class_name: ClassVar[str] = "Genome"
    class_model_uri: ClassVar[URIRef] = CHROMOSCHEMA.Genome

    id: Union[str, GenomeId] = None
    name: Union[str, LabelType] = None
    taxon: Optional[Union[str, TaxonIdentifier]] = None
    build: Optional[Union[str, GenomeBuildId]] = None
    previous_builds: Optional[Union[Union[str, GenomeBuildId], List[Union[str, GenomeBuildId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenomeId):
            self.id = GenomeId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.taxon is not None and not isinstance(self.taxon, TaxonIdentifier):
            self.taxon = TaxonIdentifier(self.taxon)

        if self.build is not None and not isinstance(self.build, GenomeBuildId):
            self.build = GenomeBuildId(self.build)

        if not isinstance(self.previous_builds, list):
            self.previous_builds = [self.previous_builds] if self.previous_builds is not None else []
        self.previous_builds = [v if isinstance(v, GenomeBuildId) else GenomeBuildId(v) for v in self.previous_builds]

        super().__post_init__(**kwargs)


@dataclass
class GenomeBuild(YAMLRoot):
    """
    Represents a specific build of a sequenced genome
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHROMOSCHEMA.GenomeBuild
    class_class_curie: ClassVar[str] = "chromoschema:GenomeBuild"
    class_name: ClassVar[str] = "GenomeBuild"
    class_model_uri: ClassVar[URIRef] = CHROMOSCHEMA.GenomeBuild

    id: Union[str, GenomeBuildId] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenomeBuildId):
            self.id = GenomeBuildId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class OrganismTaxon(YAMLRoot):
    """
    Represents a species, e.g. Homo sapiens
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxon
    class_class_curie: ClassVar[str] = "biolink:OrganismTaxon"
    class_name: ClassVar[str] = "OrganismTaxon"
    class_model_uri: ClassVar[URIRef] = CHROMOSCHEMA.OrganismTaxon

    id: Union[str, OrganismTaxonId] = None
    name: Optional[Union[str, LabelType]] = None
    common_name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismTaxonId):
            self.id = OrganismTaxonId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.common_name is not None and not isinstance(self.common_name, LabelType):
            self.common_name = LabelType(self.common_name)

        super().__post_init__(**kwargs)


# Enumerations
class EntityType(EnumDefinitionImpl):
    """
    SO or GO type
    """
    chromosome = PermissibleValue(text="chromosome",
                                           meaning=GO["0005694"])
    chromosome_part = PermissibleValue(text="chromosome_part",
                                                     meaning=GO["0098687"])

    _defn = EnumDefinition(
        name="EntityType",
        description="SO or GO type",
    )

class AutosomeVsSexChromosome(EnumDefinitionImpl):
    """
    sex or autosome
    """
    sex_chromosome = PermissibleValue(text="sex_chromosome",
                                                   meaning=GO["0000803"])
    autosome = PermissibleValue(text="autosome",
                                       meaning=GO["0030849"])

    _defn = EnumDefinition(
        name="AutosomeVsSexChromosome",
        description="sex or autosome",
    )

class SexChromosomeType(EnumDefinitionImpl):
    """
    what type of sex chromosome
    """
    X = PermissibleValue(text="X",
                         meaning=GO["0000805"])
    Y = PermissibleValue(text="Y",
                         meaning=GO["0000806"])
    W = PermissibleValue(text="W",
                         meaning=GO["0000804"])
    Z = PermissibleValue(text="Z",
                         meaning=GO["0000807"])

    _defn = EnumDefinition(
        name="SexChromosomeType",
        description="what type of sex chromosome",
    )

class LocationType(EnumDefinitionImpl):
    """
    where in the cell
    """
    nucleus = PermissibleValue(text="nucleus",
                                     meaning=GO["0005634"])
    mitochondrion = PermissibleValue(text="mitochondrion",
                                                 meaning=GO["0005739"])

    _defn = EnumDefinition(
        name="LocationType",
        description="where in the cell",
    )

class ChromatinType(EnumDefinitionImpl):

    heterochromatin = PermissibleValue(text="heterochromatin",
                                                     meaning=GO["0000792"])
    euchromatin = PermissibleValue(text="euchromatin",
                                             meaning=GO["0000791"])

    _defn = EnumDefinition(
        name="ChromatinType",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=CHROMOSCHEMA.id, name="id", curie=CHROMOSCHEMA.curie('id'),
                   model_uri=CHROMOSCHEMA.id, domain=None, range=URIRef,
                   pattern=re.compile(r'^CHR:\\S+$'))

slots.band_descriptor = Slot(uri=CHROMOSCHEMA.band_descriptor, name="band_descriptor", curie=CHROMOSCHEMA.curie('band_descriptor'),
                   model_uri=CHROMOSCHEMA.band_descriptor, domain=None, range=Optional[Union[str, BandDescriptor]])

slots.chromosome_name = Slot(uri=CHROMOSCHEMA.chromosome_name, name="chromosome_name", curie=CHROMOSCHEMA.curie('chromosome_name'),
                   model_uri=CHROMOSCHEMA.chromosome_name, domain=None, range=Optional[Union[str, ChromosomeNameType]])

slots.build = Slot(uri=BIOLINK.genome_build, name="build", curie=BIOLINK.curie('genome_build'),
                   model_uri=CHROMOSCHEMA.build, domain=None, range=Optional[Union[str, GenomeBuildId]])

slots.previous_builds = Slot(uri=CHROMOSCHEMA.previous_builds, name="previous_builds", curie=CHROMOSCHEMA.curie('previous_builds'),
                   model_uri=CHROMOSCHEMA.previous_builds, domain=None, range=Optional[Union[Union[str, GenomeBuildId], List[Union[str, GenomeBuildId]]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=CHROMOSCHEMA.name, domain=None, range=Optional[Union[str, LabelType]])

slots.common_name = Slot(uri=OIO.hasExactSynonym, name="common_name", curie=OIO.curie('hasExactSynonym'),
                   model_uri=CHROMOSCHEMA.common_name, domain=None, range=Optional[Union[str, LabelType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=CHROMOSCHEMA.type, domain=None, range=Optional[Union[str, "EntityType"]])

slots.somal_type = Slot(uri=CHROMOSCHEMA.somal_type, name="somal_type", curie=CHROMOSCHEMA.curie('somal_type'),
                   model_uri=CHROMOSCHEMA.somal_type, domain=None, range=Optional[Union[str, "AutosomeVsSexChromosome"]])

slots.sex_chromosome_type = Slot(uri=CHROMOSCHEMA.sex_chromosome_type, name="sex_chromosome_type", curie=CHROMOSCHEMA.curie('sex_chromosome_type'),
                   model_uri=CHROMOSCHEMA.sex_chromosome_type, domain=None, range=Optional[Union[str, "SexChromosomeType"]])

slots.cell_location = Slot(uri=BFO['0000050'], name="cell_location", curie=BFO.curie('0000050'),
                   model_uri=CHROMOSCHEMA.cell_location, domain=None, range=Optional[Union[str, "LocationType"]])

slots.taxon = Slot(uri=RO['0002162'], name="taxon", curie=RO.curie('0002162'),
                   model_uri=CHROMOSCHEMA.taxon, domain=None, range=Optional[Union[str, TaxonIdentifier]])

slots.start = Slot(uri=GFF.start, name="start", curie=GFF.curie('start'),
                   model_uri=CHROMOSCHEMA.start, domain=None, range=Optional[int])

slots.end = Slot(uri=GFF.end, name="end", curie=GFF.curie('end'),
                   model_uri=CHROMOSCHEMA.end, domain=None, range=Optional[int])

slots.strand = Slot(uri=GFF.strand, name="strand", curie=GFF.curie('strand'),
                   model_uri=CHROMOSCHEMA.strand, domain=None, range=Union[int, StrandType])

slots.children = Slot(uri=BFO['0000051'], name="children", curie=BFO.curie('0000051'),
                   model_uri=CHROMOSCHEMA.children, domain=None, range=Optional[Union[Union[str, ChromosomePartId], List[Union[str, ChromosomePartId]]]])

slots.parent = Slot(uri=BFO['0000050'], name="parent", curie=BFO.curie('0000050'),
                   model_uri=CHROMOSCHEMA.parent, domain=None, range=Optional[Union[str, ChromosomePartId]])

slots.exact_synonyms = Slot(uri=OIO.hasExactSynonym, name="exact_synonyms", curie=OIO.curie('hasExactSynonym'),
                   model_uri=CHROMOSCHEMA.exact_synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.broad_synonyms = Slot(uri=OIO.hasBroadSynonym, name="broad_synonyms", curie=OIO.curie('hasBroadSynonym'),
                   model_uri=CHROMOSCHEMA.broad_synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.exact_mappings = Slot(uri=SKOS.exactMatch, name="exact_mappings", curie=SKOS.curie('exactMatch'),
                   model_uri=CHROMOSCHEMA.exact_mappings, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.download_url = Slot(uri=CHROMOSCHEMA.download_url, name="download_url", curie=CHROMOSCHEMA.curie('download_url'),
                   model_uri=CHROMOSCHEMA.download_url, domain=None, range=Optional[Union[str, URI]])

slots.chromosomePartCollection__name = Slot(uri=CHROMOSCHEMA.name, name="chromosomePartCollection__name", curie=CHROMOSCHEMA.curie('name'),
                   model_uri=CHROMOSCHEMA.chromosomePartCollection__name, domain=None, range=Optional[str])

slots.chromosomePartCollection__has = Slot(uri=DCTERMS.hasPart, name="chromosomePartCollection__has", curie=DCTERMS.curie('hasPart'),
                   model_uri=CHROMOSCHEMA.chromosomePartCollection__has, domain=None, range=Optional[Union[Dict[Union[str, ChromosomePartId], Union[dict, ChromosomePart]], List[Union[dict, ChromosomePart]]]])

slots.chromosomePartCollection__genomes = Slot(uri=DCTERMS.hasPart, name="chromosomePartCollection__genomes", curie=DCTERMS.curie('hasPart'),
                   model_uri=CHROMOSCHEMA.chromosomePartCollection__genomes, domain=None, range=Optional[Union[Dict[Union[str, GenomeId], Union[dict, Genome]], List[Union[dict, Genome]]]])

slots.chromosomePartCollection__taxons = Slot(uri=DCTERMS.hasPart, name="chromosomePartCollection__taxons", curie=DCTERMS.curie('hasPart'),
                   model_uri=CHROMOSCHEMA.chromosomePartCollection__taxons, domain=None, range=Optional[Union[Dict[Union[str, OrganismTaxonId], Union[dict, OrganismTaxon]], List[Union[dict, OrganismTaxon]]]])

slots.ChromosomePart_id = Slot(uri=CHROMOSCHEMA.id, name="ChromosomePart_id", curie=CHROMOSCHEMA.curie('id'),
                   model_uri=CHROMOSCHEMA.ChromosomePart_id, domain=ChromosomePart, range=Union[str, ChromosomePartId],
                   pattern=re.compile(r'^CHR:\\S+$'))

slots.Genome_id = Slot(uri=CHROMOSCHEMA.id, name="Genome_id", curie=CHROMOSCHEMA.curie('id'),
                   model_uri=CHROMOSCHEMA.Genome_id, domain=Genome, range=Union[str, GenomeId],
                   pattern=re.compile(r'^\\w+$'))

slots.Genome_name = Slot(uri=CHROMOSCHEMA.name, name="Genome_name", curie=CHROMOSCHEMA.curie('name'),
                   model_uri=CHROMOSCHEMA.Genome_name, domain=Genome, range=Union[str, LabelType])

slots.Genome_build = Slot(uri=CHROMOSCHEMA.build, name="Genome_build", curie=CHROMOSCHEMA.curie('build'),
                   model_uri=CHROMOSCHEMA.Genome_build, domain=Genome, range=Optional[Union[str, GenomeBuildId]])

slots.GenomeBuild_id = Slot(uri=CHROMOSCHEMA.id, name="GenomeBuild_id", curie=CHROMOSCHEMA.curie('id'),
                   model_uri=CHROMOSCHEMA.GenomeBuild_id, domain=GenomeBuild, range=Union[str, GenomeBuildId],
                   pattern=re.compile(r'^CHR:\\S+$'))
