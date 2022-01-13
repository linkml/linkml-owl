# Auto generated from mondo_dps.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-01-11T22:15:31
# Schema: mondo
#
# id: https://example.org/mondo/
# description:
# license:

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
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


metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://example.org/mondo/')


# Types
class String(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = URIRef("https://example.org/mondo/String")


# Class references
class OntologyClassId(extended_str):
    pass


class OntologyClassTemplateId(extended_str):
    pass


class OntologyClassSubsetId(extended_str):
    pass


class OwlThingClassId(extended_str):
    pass


class LocationTopTemplateId(extended_str):
    pass


class DiseaseClassId(extended_str):
    pass


class MaterialEntityClassId(extended_str):
    pass


class EnvironmentalStimulusTemplateId(extended_str):
    pass


class AnatomicalStructureClassId(extended_str):
    pass


class SpecificInfectiousDiseaseByLocationTemplateId(extended_str):
    pass


class AutoimmuneInflammationTemplateId(extended_str):
    pass


class AcquiredTemplateId(extended_str):
    pass


class CarcinomaInSituTemplateId(extended_str):
    pass


class AllergicFormOfDiseaseTemplateId(extended_str):
    pass


class AcuteTemplateId(extended_str):
    pass


class NuclearSubtypeTemplateId(extended_str):
    pass


class InfantileTemplateId(extended_str):
    pass


class XLinkedTemplateId(extended_str):
    pass


class IdiopathicTemplateId(extended_str):
    pass


class ChronicTemplateId(extended_str):
    pass


class MelanomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class SpecificInflammatoryDiseaseBySiteTemplateId(extended_str):
    pass


class SmallCellCarcinomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class RareTemplateId(extended_str):
    pass


class GeneticTemplateId(extended_str):
    pass


class OrganismClassId(extended_str):
    pass


class GeneClassId(extended_str):
    pass


class ModeOfInheritanceClassId(extended_str):
    pass


class DiseaseSeriesByGeneAndInheritanceTemplateId(extended_str):
    pass


class DiseaseByDysfunctionalStructureTemplateId(extended_str):
    pass


class NeoplasmTemplateId(extended_str):
    pass


class IsolatedTemplateId(extended_str):
    pass


class ChemicalClassId(extended_str):
    pass


class DependenceOnSubstanceTemplateId(extended_str):
    pass


class CongenitalTemplateId(extended_str):
    pass


class ChildhoodTemplateId(extended_str):
    pass


class AdultTemplateId(extended_str):
    pass


class AnatomicalEntityOrCellClassId(extended_str):
    pass


class LocationTemplateId(extended_str):
    pass


class DiseaseOrDisorderClassId(extended_str):
    pass


class InheritedSusceptibilityTemplateId(extended_str):
    pass


class AdenocarcinomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class LipomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class AnatomicalEntityClassId(extended_str):
    pass


class MeningiomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplateId(extended_str):
    pass


class InfectiousDiseaseClassId(extended_str):
    pass


class PostinfectiousDiseaseTemplateId(extended_str):
    pass


class ProcessClassId(extended_str):
    pass


class BasisInDisruptionOfProcessTemplateId(extended_str):
    pass


class DiseaseSeriesByGeneTemplateId(extended_str):
    pass


class LeiomyomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class RhabdomyosarcomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class VectorBorneDiseaseTemplateId(extended_str):
    pass


class InflammatoryDiseaseBySiteTemplateId(extended_str):
    pass


class YLinkedTemplateId(extended_str):
    pass


class NeoendocrineNeoplasmTemplateId(extended_str):
    pass


class OMIMPhenotypicSeriesTemplateId(extended_str):
    pass


class LeiomyosarcomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class CancerTemplateId(extended_str):
    pass


class NeoendocrineNeoplasmGrade1TemplateId(extended_str):
    pass


class InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplateId(extended_str):
    pass


class BenignNeoplasmTemplateId(extended_str):
    pass


class CarcinomaTemplateId(extended_str):
    pass


class InfectiousDiseaseByAgentTemplateId(extended_str):
    pass


class RareGeneticTemplateId(extended_str):
    pass


class XDiseaseHasBasisInDysfunctionOfXTemplateId(extended_str):
    pass


class SubstanceAbuseTemplateId(extended_str):
    pass


class HemangiomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class ConsequenceOfInfectiousDiseaseTemplateId(extended_str):
    pass


class InbornMetabolicTemplateId(extended_str):
    pass


class MalignantTemplateId(extended_str):
    pass


class AllergyTemplateId(extended_str):
    pass


class MitochondriaalSubtypeTemplateId(extended_str):
    pass


class InfectiousInflammationTemplateId(extended_str):
    pass


class NeoplasmClassId(extended_str):
    pass


class BenignTemplateId(extended_str):
    pass


class MucoepidermoidCarcinomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class AutosomalDominantTemplateId(extended_str):
    pass


class PrimaryInfectiousTemplateId(extended_str):
    pass


class LymphomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class MulticellularAnatomicalStructureClassId(extended_str):
    pass


class AdenosquamousCarcinomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class XDiseaseDisruptsXTemplateId(extended_str):
    pass


class PoisoningTemplateId(extended_str):
    pass


class SusceptibilityByGeneTemplateId(extended_str):
    pass


class OMIMDiseaseSeriesByGeneTemplateId(extended_str):
    pass


class AutoimmuneTemplateId(extended_str):
    pass


class AdenomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class HereditaryTemplateId(extended_str):
    pass


class JuvenileTemplateId(extended_str):
    pass


class SquamousCellCarcinomaDiseaseHasLocationXTemplateId(extended_str):
    pass


class ExposureEventClassId(extended_str):
    pass


class DiseaseRealizedInResponseToEnvironmentalExposureTemplateId(extended_str):
    pass


class SarcomaTemplateId(extended_str):
    pass


class SyndromicTemplateId(extended_str):
    pass


class AutosomalRecessiveTemplateId(extended_str):
    pass


class RefractoryTemplateId(extended_str):
    pass


@dataclass
class OntologyClass(YAMLRoot):
    """
    Instance of OWL Class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OntologyClass")

    id: Union[str, OntologyClassId] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClassTemplate(YAMLRoot):
    """
    Instances of OWL classes that conform to a template
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OntologyClassTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OntologyClassTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OntologyClassTemplate")

    id: Union[str, OntologyClassTemplateId] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassTemplateId):
            self.id = OntologyClassTemplateId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClassSubset(YAMLRoot):
    """
    Mixin for instances of OWL Classes that are used as range references
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OntologyClassSubset")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OntologyClassSubset"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OntologyClassSubset")

    id: Union[str, OntologyClassSubsetId] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassSubsetId):
            self.id = OntologyClassSubsetId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class OwlThingClass(YAMLRoot):
    """
    Any subclass of owl_thing (owl_thing)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OwlThingClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OwlThingClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OwlThingClass")

    id: Union[str, OwlThingClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OwlThingClassId):
            self.id = OwlThingClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class LocationTopTemplate(YAMLRoot):
    """
    TBD.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LocationTopTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "LocationTopTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LocationTopTemplate")

    id: Union[str, LocationTopTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocationTopTemplateId):
            self.id = LocationTopTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseClass(YAMLRoot):
    """
    Any subclass of disease (disease)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DiseaseClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseClass")

    id: Union[str, DiseaseClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseClassId):
            self.id = DiseaseClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntityClass(YAMLRoot):
    """
    Any subclass of BFO:0000040 ('material entity')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MaterialEntityClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MaterialEntityClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MaterialEntityClass")

    id: Union[str, MaterialEntityClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityClassId):
            self.id = MaterialEntityClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalStimulusTemplate(YAMLRoot):
    """
    A disease that is caused by exposure to an environmental stimulus, like the sun or pesticides. Examples: [carbon
    monoxide-induced parkinsonism](http://purl.obolibrary.org/obo/MONDO_0017639), [cocaine
    intoxication](http://purl.obolibrary.org/obo/MONDO_0019544)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/EnvironmentalStimulusTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EnvironmentalStimulusTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/EnvironmentalStimulusTemplate")

    id: Union[str, EnvironmentalStimulusTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    stimulus: Optional[Union[str, MaterialEntityClassId]] = None
    stimulus_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalStimulusTemplateId):
            self.id = EnvironmentalStimulusTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.stimulus is not None and not isinstance(self.stimulus, MaterialEntityClassId):
            self.stimulus = MaterialEntityClassId(self.stimulus)

        if self.stimulus_label is not None and not isinstance(self.stimulus_label, str):
            self.stimulus_label = str(self.stimulus_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalStructureClass(YAMLRoot):
    """
    Any subclass of UBERON:0000061 ('anatomical structure')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AnatomicalStructureClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnatomicalStructureClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AnatomicalStructureClass")

    id: Union[str, AnatomicalStructureClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalStructureClassId):
            self.id = AnatomicalStructureClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class SpecificInfectiousDiseaseByLocationTemplate(YAMLRoot):
    """
    TODO
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SpecificInfectiousDiseaseByLocationTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SpecificInfectiousDiseaseByLocationTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SpecificInfectiousDiseaseByLocationTemplate")

    id: Union[str, SpecificInfectiousDiseaseByLocationTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    location: Optional[Union[str, AnatomicalStructureClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificInfectiousDiseaseByLocationTemplateId):
            self.id = SpecificInfectiousDiseaseByLocationTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.location is not None and not isinstance(self.location, AnatomicalStructureClassId):
            self.location = AnatomicalStructureClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AutoimmuneInflammationTemplate(YAMLRoot):
    """
    An instance of an autoimmune disease that is described by inflammation in a specific anatomical entity.
    Example: [autoimmune thyroid disease](http://purl.obolibrary.org/obo/MONDO_0005623)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AutoimmuneInflammationTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AutoimmuneInflammationTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AutoimmuneInflammationTemplate")

    id: Union[str, AutoimmuneInflammationTemplateId] = None
    location: Optional[Union[str, AnatomicalStructureClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutoimmuneInflammationTemplateId):
            self.id = AutoimmuneInflammationTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, AnatomicalStructureClassId):
            self.location = AnatomicalStructureClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AcquiredTemplate(YAMLRoot):
    """
    Pattern for extending a etiology-generic disease class to an acquired form. Here acquired means that basis for the
    disease is acquired during the individuals lifetime. It need not exclude genetic etiology, but it excludes
    inherited.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AcquiredTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AcquiredTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AcquiredTemplate")

    id: Union[str, AcquiredTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcquiredTemplateId):
            self.id = AcquiredTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class CarcinomaInSituTemplate(YAMLRoot):
    """
    This is a Design pattern for classes representing in situ carcinomas based on their location.
    Examples: [breast carcinoma in situ](http://purl.obolibrary.org/obo/MONDO_0004658), [liver carcinoma in
    situ](http://purl.obolibrary.org/obo/MONDO_0004715)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/CarcinomaInSituTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CarcinomaInSituTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/CarcinomaInSituTemplate")

    id: Union[str, CarcinomaInSituTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CarcinomaInSituTemplateId):
            self.id = CarcinomaInSituTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AllergicFormOfDiseaseTemplate(YAMLRoot):
    """
    An etiological pattern that extends an etiology-generic disease to an allergic form (i.e. caused by pathological
    type I hypersensitivity reaction). The
    [allergy.yaml](https://github.com/monarch-initiative/mondo/blob/master/src/patterns/dosdp-patterns/allergy.yaml)
    pattern is to refine an existing disease by trigger.
    Examples: [allergic respiratory disease](http://purl.obolibrary.org/obo/MONDO_0000771), [atopic
    eczema](http://purl.obolibrary.org/obo/MONDO_0004980), [allergic otitis
    media](http://purl.obolibrary.org/obo/MONDO_0021202)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AllergicFormOfDiseaseTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AllergicFormOfDiseaseTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AllergicFormOfDiseaseTemplate")

    id: Union[str, AllergicFormOfDiseaseTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AllergicFormOfDiseaseTemplateId):
            self.id = AllergicFormOfDiseaseTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AcuteTemplate(YAMLRoot):
    """
    This pattern is applied to diseases that are described as having an acute onset, i.e. the sudden appearance of
    disease manifestations over a short period of time.
    Examples: [acute bronchiolitis](http://purl.obolibrary.org/obo/MONDO_0020680), [acute liver
    failure](http://purl.obolibrary.org/obo/MONDO_0019542)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AcuteTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AcuteTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AcuteTemplate")

    id: Union[str, AcuteTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcuteTemplateId):
            self.id = AcuteTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class NuclearSubtypeTemplate(YAMLRoot):
    """
    A disease that is classified as a nuclear subtype, due to a defect in a nuclear gene, such as MONDO:0009640
    'mitochondrial complex I deficiency, nuclear type'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/NuclearSubtypeTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NuclearSubtypeTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/NuclearSubtypeTemplate")

    id: Union[str, NuclearSubtypeTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NuclearSubtypeTemplateId):
            self.id = NuclearSubtypeTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class InfantileTemplate(YAMLRoot):
    """
    An instance of a disease that has an onset of signs or symptoms of disease within the first 12 months of life
    (infantile onset).
    Examples: [infant botulism](http://purl.obolibrary.org/obo/MONDO_0015804), [infantile glycine
    encephalopathy](http://purl.obolibrary.org/obo/MONDO_0017354)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InfantileTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "InfantileTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InfantileTemplate")

    id: Union[str, InfantileTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InfantileTemplateId):
            self.id = InfantileTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class XLinkedTemplate(YAMLRoot):
    """
    TBD.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/XLinkedTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "XLinkedTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/XLinkedTemplate")

    id: Union[str, XLinkedTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XLinkedTemplateId):
            self.id = XLinkedTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class IdiopathicTemplate(YAMLRoot):
    """
    This pattern is applied to diseases that are described as being idiopathic, i.e. having an uncertain or unknown
    cause.
    Examples: [idiopathic aplastic anemia](http://purl.obolibrary.org/obo/MONDO_0012197), [idiopathic avascular
    necrosis](http://purl.obolibrary.org/obo/MONDO_0018380)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/IdiopathicTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "IdiopathicTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/IdiopathicTemplate")

    id: Union[str, IdiopathicTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdiopathicTemplateId):
            self.id = IdiopathicTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class ChronicTemplate(YAMLRoot):
    """
    This pattern is applied to diseases that are described as having an chronic duration, i.e. a disease having a slow
    progressive course of indefinite duration.
    Examples: [chronic bronchitis](http://purl.obolibrary.org/obo/MONDO_0005607), [chronic hepatitis B virus
    infection](http://purl.obolibrary.org/obo/MONDO_0005366)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ChronicTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ChronicTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ChronicTemplate")

    id: Union[str, ChronicTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChronicTemplateId):
            self.id = ChronicTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class MelanomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    Melanomas are malignant, usually aggressive tumor composed of atypical, neoplastic melanocytes. This is a design
    pattern for classes representing melanomas based on their location. This may be the site of origin, but it can
    also represent a secondary site for metastatized cancer. We use the generic 'disease has location' relation, which
    generalized over primary and secondary sites.
    Examples: [cutaneous melanoma](http://purl.obolibrary.org/obo/MONDO_0005012), [malignant breast
    melanoma](http://purl.obolibrary.org/obo/MONDO_0002975), [malignant melanoma of the
    mucosa](http://purl.obolibrary.org/obo/MONDO_0015694) (22 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MelanomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MelanomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MelanomaDiseaseHasLocationXTemplate")

    id: Union[str, MelanomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MelanomaDiseaseHasLocationXTemplateId):
            self.id = MelanomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class SpecificInflammatoryDiseaseBySiteTemplate(YAMLRoot):
    """
    as for inflammatory_disease_by_site, but refining a specific disease
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SpecificInflammatoryDiseaseBySiteTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SpecificInflammatoryDiseaseBySiteTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SpecificInflammatoryDiseaseBySiteTemplate")

    id: Union[str, SpecificInflammatoryDiseaseBySiteTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    agent: Optional[Union[str, OrganismClassId]] = None
    agent_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificInflammatoryDiseaseBySiteTemplateId):
            self.id = SpecificInflammatoryDiseaseBySiteTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.agent is not None and not isinstance(self.agent, OrganismClassId):
            self.agent = OrganismClassId(self.agent)

        if self.agent_label is not None and not isinstance(self.agent_label, str):
            self.agent_label = str(self.agent_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class SmallCellCarcinomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    This is auto-generated. Add your description here
    Examples: [cervical small cell carcinoma](http://purl.obolibrary.org/obo/MONDO_0006142), [pancreatic small cell
    neuroendocrine carcinoma](http://purl.obolibrary.org/obo/MONDO_0006348), [ureter small cell
    carcinoma](http://purl.obolibrary.org/obo/MONDO_0006482) (16 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SmallCellCarcinomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SmallCellCarcinomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SmallCellCarcinomaDiseaseHasLocationXTemplate")

    id: Union[str, SmallCellCarcinomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SmallCellCarcinomaDiseaseHasLocationXTemplateId):
            self.id = SmallCellCarcinomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class RareTemplate(YAMLRoot):
    """
    TBD.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/RareTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "RareTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/RareTemplate")

    id: Union[str, RareTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RareTemplateId):
            self.id = RareTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class GeneticTemplate(YAMLRoot):
    """
    TBD.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/GeneticTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "GeneticTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/GeneticTemplate")

    id: Union[str, GeneticTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneticTemplateId):
            self.id = GeneticTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class OrganismClass(YAMLRoot):
    """
    Any subclass of NCBITaxon:1 ('organism')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OrganismClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OrganismClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OrganismClass")

    id: Union[str, OrganismClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismClassId):
            self.id = OrganismClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class GeneClass(YAMLRoot):
    """
    Any subclass of SO:0000704 ('gene')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/GeneClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "GeneClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/GeneClass")

    id: Union[str, GeneClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneClassId):
            self.id = GeneClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class ModeOfInheritanceClass(YAMLRoot):
    """
    Any subclass of HP:0000005 ('mode of inheritance')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ModeOfInheritanceClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ModeOfInheritanceClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ModeOfInheritanceClass")

    id: Union[str, ModeOfInheritanceClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModeOfInheritanceClassId):
            self.id = ModeOfInheritanceClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class DiseaseSeriesByGeneAndInheritanceTemplate(YAMLRoot):
    """
    This pattern is for diseases that are caused by a single mutation in a single gene, that have gene-based names,
    and are inherited by a specific mechanism, succh as autosomal dominant and autosomal recessive.
    Examples: [Growth hormone insensitivity syndrome with immune
    dysregulation](https://omim.org/phenotypicSeries/PS245590), Growth hormone insensitivity with immune dysregulation
    1, autosomal recessive and Growth hormone insensitivity with immune dysregulation 2, autosomal dominant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseSeriesByGeneAndInheritanceTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DiseaseSeriesByGeneAndInheritanceTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseSeriesByGeneAndInheritanceTemplate")

    id: Union[str, DiseaseSeriesByGeneAndInheritanceTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    gene: Optional[Union[str, GeneClassId]] = None
    gene_label: Optional[str] = None
    mode_of_inheritance: Optional[Union[str, ModeOfInheritanceClassId]] = None
    mode_of_inheritance_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseSeriesByGeneAndInheritanceTemplateId):
            self.id = DiseaseSeriesByGeneAndInheritanceTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.gene is not None and not isinstance(self.gene, GeneClassId):
            self.gene = GeneClassId(self.gene)

        if self.gene_label is not None and not isinstance(self.gene_label, str):
            self.gene_label = str(self.gene_label)

        if self.mode_of_inheritance is not None and not isinstance(self.mode_of_inheritance, ModeOfInheritanceClassId):
            self.mode_of_inheritance = ModeOfInheritanceClassId(self.mode_of_inheritance)

        if self.mode_of_inheritance_label is not None and not isinstance(self.mode_of_inheritance_label, str):
            self.mode_of_inheritance_label = str(self.mode_of_inheritance_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseByDysfunctionalStructureTemplate(YAMLRoot):
    """
    Diseases classified by a perturbation in an anatomical structure (such as a subcellular component, or an organ)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseByDysfunctionalStructureTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DiseaseByDysfunctionalStructureTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseByDysfunctionalStructureTemplate")

    id: Union[str, DiseaseByDysfunctionalStructureTemplateId] = None
    structure: Optional[Union[str, AnatomicalStructureClassId]] = None
    structure_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseByDysfunctionalStructureTemplateId):
            self.id = DiseaseByDysfunctionalStructureTemplateId(self.id)

        if self.structure is not None and not isinstance(self.structure, AnatomicalStructureClassId):
            self.structure = AnatomicalStructureClassId(self.structure)

        if self.structure_label is not None and not isinstance(self.structure_label, str):
            self.structure_label = str(self.structure_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class NeoplasmTemplate(YAMLRoot):
    """
    TBD.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/NeoplasmTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NeoplasmTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/NeoplasmTemplate")

    id: Union[str, NeoplasmTemplateId] = None
    structure: Optional[Union[str, OwlThingClassId]] = None
    structure_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NeoplasmTemplateId):
            self.id = NeoplasmTemplateId(self.id)

        if self.structure is not None and not isinstance(self.structure, OwlThingClassId):
            self.structure = OwlThingClassId(self.structure)

        if self.structure_label is not None and not isinstance(self.structure_label, str):
            self.structure_label = str(self.structure_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class IsolatedTemplate(YAMLRoot):
    """
    Some diseases exist in both isolated and syndromic forms. For example, aniridia ([MONDO_0019172
    aniridia](http://purl.obolibrary.org/obo/MONDO_0019172), [MONDO_0020148'syndromic
    aniridia'](http://purl.obolibrary.org/obo/MONDO_0020148) and [MONDO_0007119 'isolated
    aniridia'](http://purl.obolibrary.org/obo/MONDO_0007119). Use this pattern to define the isolated form of a
    disease when a term exists for the isolated/syndromic-neutral version. In general, this pattern should be used in
    parallel with syndromic. E.g. if you make a term 'syndromic disease, you should also have 'isolated disease' [see
    pattern here(https://github.com/monarch-initiative/mondo/blob/master/src/patterns/dosdp-patterns/syndromic.yaml).
    Note that the isolated and syndromic forms will be inferred to be disjoint due to the GCI pattern.
    Examples: ['isolated aniridia'](http://purl.obolibrary.org/obo/MONDO_0007119), ['isolated
    dystonia'](http://purl.obolibrary.org/obo/MONDO_0015494), ['isolated focal palmoplantar
    keratoderma'](http://purl.obolibrary.org/obo/MONDO_0017673)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/IsolatedTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "IsolatedTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/IsolatedTemplate")

    id: Union[str, IsolatedTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsolatedTemplateId):
            self.id = IsolatedTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalClass(YAMLRoot):
    """
    Any subclass of CHEBI:24431 ('chemical')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ChemicalClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ChemicalClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ChemicalClass")

    id: Union[str, ChemicalClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalClassId):
            self.id = ChemicalClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class DependenceOnSubstanceTemplate(YAMLRoot):
    """
    Dependence on a substance that specifies the environmental stimulus such as alcohol, cocaine, etc. Example:
    [dependence on cocaine](http://purl.obolibrary.org/obo/MONDO_0005186).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DependenceOnSubstanceTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DependenceOnSubstanceTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DependenceOnSubstanceTemplate")

    id: Union[str, DependenceOnSubstanceTemplateId] = None
    stimulus: Optional[Union[str, ChemicalClassId]] = None
    stimulus_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DependenceOnSubstanceTemplateId):
            self.id = DependenceOnSubstanceTemplateId(self.id)

        if self.stimulus is not None and not isinstance(self.stimulus, ChemicalClassId):
            self.stimulus = ChemicalClassId(self.stimulus)

        if self.stimulus_label is not None and not isinstance(self.stimulus_label, str):
            self.stimulus_label = str(self.stimulus_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class CongenitalTemplate(YAMLRoot):
    """
    An instance of a disease in which the disease is present at birth, regardless of cause.
    Examples: [congenital agammaglobulinemia](http://purl.obolibrary.org/obo/MONDO_0001902), [congenital
    nystagmus](http://purl.obolibrary.org/obo/MONDO_0005712)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/CongenitalTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CongenitalTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/CongenitalTemplate")

    id: Union[str, CongenitalTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CongenitalTemplateId):
            self.id = CongenitalTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class ChildhoodTemplate(YAMLRoot):
    """
    An instance of a disease that has an onset of signs or symptoms of disease between the age of 1 to 5 years
    (childhood onset).
    Examples: [childhood astrocytic tumor](http://purl.obolibrary.org/obo/MONDO_0002505), [childhood malignant
    melanoma](http://purl.obolibrary.org/obo/MONDO_0042494)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ChildhoodTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ChildhoodTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ChildhoodTemplate")

    id: Union[str, ChildhoodTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChildhoodTemplateId):
            self.id = ChildhoodTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AdultTemplate(YAMLRoot):
    """
    An instance of a disease that has an onset of signs or symptoms of disease between the age of 16 years or later
    (adult onset).
    Examples: [adult brain stem neoplasm](http://purl.obolibrary.org/obo/MONDO_0024797), [adult-onset myasthenia
    gravis](http://purl.obolibrary.org/obo/MONDO_0018324)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AdultTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AdultTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AdultTemplate")

    id: Union[str, AdultTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdultTemplateId):
            self.id = AdultTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntityOrCellClass(YAMLRoot):
    """
    Any subclass of 'anatomical entity' or 'cell' ('anatomical entity' or 'cell')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AnatomicalEntityOrCellClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnatomicalEntityOrCellClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AnatomicalEntityOrCellClass")

    id: Union[str, AnatomicalEntityOrCellClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityOrCellClassId):
            self.id = AnatomicalEntityOrCellClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class LocationTemplate(YAMLRoot):
    """
    A disease that is located in a specific anatomical site.
    Examples: ['abdominal cystic lymphangioma'](http://purl.obolibrary.org/obo/MONDO_0021726), ['articular cartilage
    disease'](http://purl.obolibrary.org/obo/MONDO_0003816), ['urethral
    disease'](http://purl.obolibrary.org/obo/MONDO_0004184)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LocationTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "LocationTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LocationTemplate")

    id: Union[str, LocationTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    location: Optional[Union[str, AnatomicalEntityOrCellClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocationTemplateId):
            self.id = LocationTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.location is not None and not isinstance(self.location, AnatomicalEntityOrCellClassId):
            self.location = AnatomicalEntityOrCellClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrDisorderClass(YAMLRoot):
    """
    Any subclass of MONDO:0000001 ('disease or disorder')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseOrDisorderClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DiseaseOrDisorderClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseOrDisorderClass")

    id: Union[str, DiseaseOrDisorderClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseOrDisorderClassId):
            self.id = DiseaseOrDisorderClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class InheritedSusceptibilityTemplate(YAMLRoot):
    """
    This pattern should be used for children of MONDO_0020573'inherited disease susceptibility', including OMIM
    phenotypic series (OMIMPS) for which the subclasses are susceptibilities. Note, this pattern should not have an
    asserted causative gene as logical axiom (and no single causative gene in text definition), in those cases, the
    susceptibility_by_gene pattern should be used instead. The children should have asserted causative genes in the
    text definitions and in the logical axioms. This pattern is a superclass of the susceptibility_by_gene pattern.
    Examples: ['microvascular complications of diabetes,
    susceptibility'](http://purl.obolibrary.org/obo/MONDO_0000065), ['epilepsy, idiopathic
    generalized'](http://purl.obolibrary.org/obo/MONDO_0005579), ['aspergillosis, susceptibility
    to'](http://purl.obolibrary.org/obo/MONDO_0013562).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InheritedSusceptibilityTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "InheritedSusceptibilityTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InheritedSusceptibilityTemplate")

    id: Union[str, InheritedSusceptibilityTemplateId] = None
    disease: Optional[Union[str, DiseaseOrDisorderClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InheritedSusceptibilityTemplateId):
            self.id = InheritedSusceptibilityTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseOrDisorderClassId):
            self.disease = DiseaseOrDisorderClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AdenocarcinomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    Adenocarcinoma is a common cancer characterized by the presence of malignant glandular cells. This is a design
    pattern for classes representing adenocarcinomas based on their location. This may be the site of origin, but it
    can also represent a secondary site for metastatized cancer. We use the generic disease has location relation,
    which generalized over primary and secondary sites.
    Examples: [adenocarcinoma of cervix uteri](http://purl.obolibrary.org/obo/MONDO_0016275), [pituitary
    adenocarcinoma (disease)](http://purl.obolibrary.org/obo/MONDO_0017582)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AdenocarcinomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AdenocarcinomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AdenocarcinomaDiseaseHasLocationXTemplate")

    id: Union[str, AdenocarcinomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdenocarcinomaDiseaseHasLocationXTemplateId):
            self.id = AdenocarcinomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class LipomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    A benign, usually painless, well-circumscribed lipomatous tumor composed of adipose tissue that is located in a
    specific anatomical location.
    Examples: [skin lipoma](http://purl.obolibrary.org/obo/MONDO_0000964), [colorectal
    lipoma](http://purl.obolibrary.org/obo/MONDO_0003885), [tendon sheath
    lipoma](http://purl.obolibrary.org/obo/MONDO_0004076) (28 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LipomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "LipomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LipomaDiseaseHasLocationXTemplate")

    id: Union[str, LipomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LipomaDiseaseHasLocationXTemplateId):
            self.id = LipomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntityClass(YAMLRoot):
    """
    Any subclass of UBERON:0001062 ('anatomical entity')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AnatomicalEntityClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnatomicalEntityClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AnatomicalEntityClass")

    id: Union[str, AnatomicalEntityClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityClassId):
            self.id = AnatomicalEntityClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class MeningiomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    A meningioma is a slow growing tumor attached to the dura mater. This is a design pattern for classes representing
    meningiomas based on their location. This may be the site of origin, but it can also represent a secondary site
    for metastatized cancer. We use the generic 'disease has location' relation, which generalized over primary and
    secondary sites.
    Examples: [skin meningioma](http://purl.obolibrary.org/obo/MONDO_0004429), [brain
    meningioma](http://purl.obolibrary.org/obo/MONDO_0000642), [choroid plexus
    meningioma](http://purl.obolibrary.org/obo/MONDO_0003053) (26 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MeningiomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MeningiomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MeningiomaDiseaseHasLocationXTemplate")

    id: Union[str, MeningiomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, AnatomicalEntityClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeningiomaDiseaseHasLocationXTemplateId):
            self.id = MeningiomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, AnatomicalEntityClassId):
            self.location = AnatomicalEntityClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate(YAMLRoot):
    """
    A disease that disrupts a process, like immune system function, or early development.
    Examples: [type III hypersensitivity disease](http://purl.obolibrary.org/obo/MONDO_0007004), [type IV
    hypersensitivity disease](http://purl.obolibrary.org/obo/MONDO_0002459), [neural tube closure
    defect](http://purl.obolibrary.org/obo/MONDO_0017059) (55 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate")

    id: Union[str, DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplateId] = None
    process: Optional[Union[str, OwlThingClassId]] = None
    process_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplateId):
            self.id = DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplateId(self.id)

        if self.process is not None and not isinstance(self.process, OwlThingClassId):
            self.process = OwlThingClassId(self.process)

        if self.process_label is not None and not isinstance(self.process_label, str):
            self.process_label = str(self.process_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class InfectiousDiseaseClass(YAMLRoot):
    """
    Any subclass of MONDO:0005550 ('infectious disease')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InfectiousDiseaseClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "InfectiousDiseaseClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InfectiousDiseaseClass")

    id: Union[str, InfectiousDiseaseClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InfectiousDiseaseClassId):
            self.id = InfectiousDiseaseClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class PostinfectiousDiseaseTemplate(YAMLRoot):
    """
    A design pattern for conditions such as post-herpetic neuralgia or postinfectious encephalitis, where the disease
    is secondary to the initial infection.
    TODO: write better guidelines on what constitutes a secondary disease vs primary. * We do not use this pattern for
    AIDS-HIV for example, instead representing this is using SubClassOf. * We draw a distinction between infectious
    and postinfectious encepahlitis. * we do not use this pattern for chickenpox, but we do for shingles
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/PostinfectiousDiseaseTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PostinfectiousDiseaseTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/PostinfectiousDiseaseTemplate")

    id: Union[str, PostinfectiousDiseaseTemplateId] = None
    disease: Optional[Union[str, OrganismClassId]] = None
    disease_label: Optional[str] = None
    feature: Optional[Union[str, InfectiousDiseaseClassId]] = None
    feature_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostinfectiousDiseaseTemplateId):
            self.id = PostinfectiousDiseaseTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, OrganismClassId):
            self.disease = OrganismClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.feature is not None and not isinstance(self.feature, InfectiousDiseaseClassId):
            self.feature = InfectiousDiseaseClassId(self.feature)

        if self.feature_label is not None and not isinstance(self.feature_label, str):
            self.feature_label = str(self.feature_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class ProcessClass(YAMLRoot):
    """
    Any subclass of BFO:0000015 ('process')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ProcessClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ProcessClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ProcessClass")

    id: Union[str, ProcessClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessClassId):
            self.id = ProcessClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class BasisInDisruptionOfProcessTemplate(YAMLRoot):
    """
    A pattern for generic groupings of diseases based around the molecular basis for the disease in terms of a GO
    molecular function or cellular process.
    For example: DNA repair or RAS signaling
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/BasisInDisruptionOfProcessTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BasisInDisruptionOfProcessTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/BasisInDisruptionOfProcessTemplate")

    id: Union[str, BasisInDisruptionOfProcessTemplateId] = None
    process: Optional[Union[str, ProcessClassId]] = None
    process_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BasisInDisruptionOfProcessTemplateId):
            self.id = BasisInDisruptionOfProcessTemplateId(self.id)

        if self.process is not None and not isinstance(self.process, ProcessClassId):
            self.process = ProcessClassId(self.process)

        if self.process_label is not None and not isinstance(self.process_label, str):
            self.process_label = str(self.process_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseSeriesByGeneTemplate(YAMLRoot):
    """
    This pattern is for diseases that are caused by a single mutation in a single gene, that have gene-based names,
    such as new disease terms that are requested by ClinGen, like MED12-related intellectual disability syndrome.
    Examples: [MED12-related intellectual disability syndrome](http://purl.obolibrary.org/obo/MONDO_0100000),
    [TTN-related myopathy](http://purl.obolibrary.org/obo/MONDO_0100175), [MYPN-related
    myopathy](http://purl.obolibrary.org/obo/MONDO_0015023)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseSeriesByGeneTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DiseaseSeriesByGeneTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseSeriesByGeneTemplate")

    id: Union[str, DiseaseSeriesByGeneTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    gene: Optional[Union[str, GeneClassId]] = None
    gene_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseSeriesByGeneTemplateId):
            self.id = DiseaseSeriesByGeneTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.gene is not None and not isinstance(self.gene, GeneClassId):
            self.gene = GeneClassId(self.gene)

        if self.gene_label is not None and not isinstance(self.gene_label, str):
            self.gene_label = str(self.gene_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class LeiomyomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    A leiomyoma (a well-circumscribed benign smooth muscle neoplasm characterized by the presence of spindle cells
    with cigar-shaped nuclei, interlacing fascicles, and a whorled pattern) that is located in a specific anatomical
    entity.
    Examples: [leiomyoma cutis](http://purl.obolibrary.org/obo/MONDO_0003291), [ureter
    leiomyoma](http://purl.obolibrary.org/obo/MONDO_0001399), [urethra
    leiomyoma](http://purl.obolibrary.org/obo/MONDO_0002222) (30 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LeiomyomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "LeiomyomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LeiomyomaDiseaseHasLocationXTemplate")

    id: Union[str, LeiomyomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, AnatomicalEntityClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LeiomyomaDiseaseHasLocationXTemplateId):
            self.id = LeiomyomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, AnatomicalEntityClassId):
            self.location = AnatomicalEntityClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class RhabdomyosarcomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    This is auto-generated. Add your description here
    Examples: [rhabdomyosarcoma of the cervix uteri](http://purl.obolibrary.org/obo/MONDO_0016282), [breast
    rhabdomyosarcoma](http://purl.obolibrary.org/obo/MONDO_0002859), [testis
    rhabdomyosarcoma](http://purl.obolibrary.org/obo/MONDO_0002860) (15 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/RhabdomyosarcomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "RhabdomyosarcomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/RhabdomyosarcomaDiseaseHasLocationXTemplate")

    id: Union[str, RhabdomyosarcomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RhabdomyosarcomaDiseaseHasLocationXTemplateId):
            self.id = RhabdomyosarcomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class VectorBorneDiseaseTemplate(YAMLRoot):
    """
    An infectious disease where a pathogen is carried and transmitted by another organism that acts as disease vector.
    Examples: MONDO_0020601 'mosquito-borne viral encephalitis', MONDO_0017572 'tick-borne encephalitis'
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/VectorBorneDiseaseTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VectorBorneDiseaseTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/VectorBorneDiseaseTemplate")

    id: Union[str, VectorBorneDiseaseTemplateId] = None
    infectious_disease: Optional[Union[str, InfectiousDiseaseClassId]] = None
    infectious_disease_label: Optional[str] = None
    vector: Optional[Union[str, OrganismClassId]] = None
    vector_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VectorBorneDiseaseTemplateId):
            self.id = VectorBorneDiseaseTemplateId(self.id)

        if self.infectious_disease is not None and not isinstance(self.infectious_disease, InfectiousDiseaseClassId):
            self.infectious_disease = InfectiousDiseaseClassId(self.infectious_disease)

        if self.infectious_disease_label is not None and not isinstance(self.infectious_disease_label, str):
            self.infectious_disease_label = str(self.infectious_disease_label)

        if self.vector is not None and not isinstance(self.vector, OrganismClassId):
            self.vector = OrganismClassId(self.vector)

        if self.vector_label is not None and not isinstance(self.vector_label, str):
            self.vector_label = str(self.vector_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class InflammatoryDiseaseBySiteTemplate(YAMLRoot):
    """
    Inflammatory diseases can be classified by the location in which the pathological inflammatory process occurs.
    For inflammatory diseases caused by infection, this may be the site of infection.
    Examples: ['Achilles bursitis'](http://purl.obolibrary.org/obo/MONDO_0001594),
    [blepharitis](http://purl.obolibrary.org/obo/MONDO_0004785),
    [epiglottitis](http://purl.obolibrary.org/obo/MONDO_0005753)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InflammatoryDiseaseBySiteTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "InflammatoryDiseaseBySiteTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InflammatoryDiseaseBySiteTemplate")

    id: Union[str, InflammatoryDiseaseBySiteTemplateId] = None
    location: Optional[Union[str, AnatomicalStructureClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InflammatoryDiseaseBySiteTemplateId):
            self.id = InflammatoryDiseaseBySiteTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, AnatomicalStructureClassId):
            self.location = AnatomicalStructureClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class YLinkedTemplate(YAMLRoot):
    """
    TBD.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/YLinkedTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "YLinkedTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/YLinkedTemplate")

    id: Union[str, YLinkedTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, YLinkedTemplateId):
            self.id = YLinkedTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class NeoendocrineNeoplasmTemplate(YAMLRoot):
    """
    Note that tumor is typically a synonym for neoplasm, although this can be context dependent. For neuroendocrine
    tumors (NETs), NCIT uses the nomenclature 'tumor' to indicate 'well differentiated, low or intermediate grade
    tumor'. This can also be called carcinoid, see
    [https://www.cancer.org/cancer/gastrointestinal-carcinoid-tumor/about/what-is-gastrointestinal-carcinoid.html](https://www.cancer.org/cancer/gastrointestinal-carcinoid-tumor/about/what-is-gastrointestinal-carcinoid.html).
    We attempt to spell this out in our labels.
    Examples: [breast neuroendocrine neoplasm](http://purl.obolibrary.org/obo/MONDO_0002485), [digestive system
    neuroendocrine neoplasm](http://purl.obolibrary.org/obo/MONDO_0024503), [ovarian neuroendocrine
    neoplasm](http://purl.obolibrary.org/obo/MONDO_0002481)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/NeoendocrineNeoplasmTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NeoendocrineNeoplasmTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/NeoendocrineNeoplasmTemplate")

    id: Union[str, NeoendocrineNeoplasmTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NeoendocrineNeoplasmTemplateId):
            self.id = NeoendocrineNeoplasmTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class OMIMPhenotypicSeriesTemplate(YAMLRoot):
    """
    This pattern is meant to be used for OMIM phenotypic series (OMIMPS), which are represented as grouping classes in
    Mondo. Note: - every instance of this metaclass should be equivalent to (via annotated xref) to something in
    OMIMPS namespace - it will never have an asserted causative gene as logical axiom (and no single causative gene in
    text def) - it must never be equivalent to an OMIM:nnnnnn (often redundant with the above rule) - it must have an
    acronym synonym, e.g. HPE - it must have two or more subclasses (direct or indirect) that are equivalent to OMIMs
    - the subclasses should (not must) have a logical def that uses the PS as a genus (see
    http://purl.obolibrary.org/obo/mondo/patterns/disease_series_by_gene.yaml) - the OMIM subclasses must have acronym
    synonyms that are the parent syn + number, e.g. HPE1, HPE2 - the primary label for the children should also be
    parent + {"type"} + number - the first member will usually have the same number local ID as the PS - the first
    member in OMIM usually has documentation that is pertinent to the parent PS - the members may(?) generally share
    high semantic similarity - All OMIMPS disease should have a has modifier some inherited restricted, see
    http://purl.obolibrary.org/obo/mondo/sparql/omimps-should-be-inherited-violation.sparql
    Examples: [holoprosencephaly](http://purl.obolibrary.org/obo/MONDO_0016296)
    [OMIMPS:236100](https://omim.org/phenotypicSeries/PS236100), '3-M
    syndrome'(http://purl.obolibrary.org/obo/MONDO_0007477)
    [OMIMPS:236100](https://omim.org/phenotypicSeries/PS273750).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OMIMPhenotypicSeriesTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OMIMPhenotypicSeriesTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OMIMPhenotypicSeriesTemplate")

    id: Union[str, OMIMPhenotypicSeriesTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OMIMPhenotypicSeriesTemplateId):
            self.id = OMIMPhenotypicSeriesTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class LeiomyosarcomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    An uncommon, aggressive malignant smooth muscle neoplasm, usually occurring in post-menopausal women that is
    characterized by a proliferation of neoplastic spindle cells that is located in a specific anatomical location.
    Examples: [leiomyosarcoma of the cervix uteri](http://purl.obolibrary.org/obo/MONDO_0016283), [cutaneous
    leiomyosarcoma (disease)](http://purl.obolibrary.org/obo/MONDO_0003362), [breast
    leiomyosarcoma](http://purl.obolibrary.org/obo/MONDO_0003371) (29 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LeiomyosarcomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "LeiomyosarcomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LeiomyosarcomaDiseaseHasLocationXTemplate")

    id: Union[str, LeiomyosarcomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LeiomyosarcomaDiseaseHasLocationXTemplateId):
            self.id = LeiomyosarcomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class CancerTemplate(YAMLRoot):
    """
    Cancers are malignant neoplasms arising from a variety of different cell types.
    This is a design pattern for classes representing cancers based on their location. This may be the site of origin,
    but it can also represent a secondary site for metastatized cancer.
    We use the generic 'disease has location' relation, which generalized over primary and secondary sites.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/CancerTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CancerTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/CancerTemplate")

    id: Union[str, CancerTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CancerTemplateId):
            self.id = CancerTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class NeoendocrineNeoplasmGrade1Template(YAMLRoot):
    """
    We follow NCIT in making carcinoid tumor a synonym for neuroendocrine neoplasm G1 (G1 NET).
    Examples: [carcinoid tumor (disease)](http://purl.obolibrary.org/obo/MONDO_0005369)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/NeoendocrineNeoplasmGrade1Template")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NeoendocrineNeoplasmGrade1Template"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/NeoendocrineNeoplasmGrade1Template")

    id: Union[str, NeoendocrineNeoplasmGrade1TemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NeoendocrineNeoplasmGrade1TemplateId):
            self.id = NeoendocrineNeoplasmGrade1TemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate(YAMLRoot):
    """
    This pattern is used for inborn errors of metabolism that cause disruption of a specific biological process, such
    as enzyme activity or ion transport.
    Examples: ['5-oxoprolinase deficiency (disease)'](http://purl.obolibrary.org/obo/MONDO_0009825), [inborn disorder
    of methionine cycle and sulfur amino acid metabolism](http://purl.obolibrary.org/obo/MONDO_0019222), [inborn
    aminoacylase deficiency](http://purl.obolibrary.org/obo/MONDO_0017686) (51 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate")

    id: Union[str, InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplateId] = None
    process: Optional[Union[str, OwlThingClassId]] = None
    process_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplateId):
            self.id = InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplateId(self.id)

        if self.process is not None and not isinstance(self.process, OwlThingClassId):
            self.process = OwlThingClassId(self.process)

        if self.process_label is not None and not isinstance(self.process_label, str):
            self.process_label = str(self.process_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class BenignNeoplasmTemplate(YAMLRoot):
    """
    Neoplasms are benign or malignant tissue growths resulting from uncontrolled cell proliferation cell types.
    This is a design pattern for classes representing *benign* neoplasms based on their location.
    See also: benign.yaml TODO: choose one over another
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/BenignNeoplasmTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BenignNeoplasmTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/BenignNeoplasmTemplate")

    id: Union[str, BenignNeoplasmTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenignNeoplasmTemplateId):
            self.id = BenignNeoplasmTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class CarcinomaTemplate(YAMLRoot):
    """
    Carcinomas are malignant neoplasms arising from epithelial cells.
    This is a Design pattern for classes representing carcinomas based on their location. This may be the site of
    origin, but it can also represent a secondary site for metastatized cancer.
    We use the generic 'disease has location' relation, which generalized over primary and secondary sites.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/CarcinomaTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CarcinomaTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/CarcinomaTemplate")

    id: Union[str, CarcinomaTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CarcinomaTemplateId):
            self.id = CarcinomaTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class InfectiousDiseaseByAgentTemplate(YAMLRoot):
    """
    Infectious diseases can be classified by the infectioos agent, such as bacteria, coronavirus, etc, that causes the
    disease.
    Examples: [COVID-19](http://purl.obolibrary.org/obo/MONDO_0100096),
    [cholera](http://purl.obolibrary.org/obo/MONDO_0015766)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InfectiousDiseaseByAgentTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "InfectiousDiseaseByAgentTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InfectiousDiseaseByAgentTemplate")

    id: Union[str, InfectiousDiseaseByAgentTemplateId] = None
    agent: Optional[Union[str, OrganismClassId]] = None
    agent_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InfectiousDiseaseByAgentTemplateId):
            self.id = InfectiousDiseaseByAgentTemplateId(self.id)

        if self.agent is not None and not isinstance(self.agent, OrganismClassId):
            self.agent = OrganismClassId(self.agent)

        if self.agent_label is not None and not isinstance(self.agent_label, str):
            self.agent_label = str(self.agent_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class RareGeneticTemplate(YAMLRoot):
    """
    TBD.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/RareGeneticTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "RareGeneticTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/RareGeneticTemplate")

    id: Union[str, RareGeneticTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RareGeneticTemplateId):
            self.id = RareGeneticTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class XDiseaseHasBasisInDysfunctionOfXTemplate(YAMLRoot):
    """
    This is auto-generated. Add your description here
    Examples: [collagenopathy type 2 alpha 1](http://purl.obolibrary.org/obo/MONDO_0022800),
    [hemoglobinopathy](http://purl.obolibrary.org/obo/MONDO_0044348), [blood platelet
    disease](http://purl.obolibrary.org/obo/MONDO_0002245) (2195 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/XDiseaseHasBasisInDysfunctionOfXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "XDiseaseHasBasisInDysfunctionOfXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/XDiseaseHasBasisInDysfunctionOfXTemplate")

    id: Union[str, XDiseaseHasBasisInDysfunctionOfXTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    structure: Optional[Union[str, OwlThingClassId]] = None
    structure_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XDiseaseHasBasisInDysfunctionOfXTemplateId):
            self.id = XDiseaseHasBasisInDysfunctionOfXTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.structure is not None and not isinstance(self.structure, OwlThingClassId):
            self.structure = OwlThingClassId(self.structure)

        if self.structure_label is not None and not isinstance(self.structure_label, str):
            self.structure_label = str(self.structure_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class SubstanceAbuseTemplate(YAMLRoot):
    """
    A substance abuse that specifies a specific environmental stimulus such as alcohol, cocaine, etc. Examples:
    [alcohol abuse](http://purl.obolibrary.org/obo/MONDO_0002046), [cocaine
    abuse](http://purl.obolibrary.org/obo/MONDO_0004456)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SubstanceAbuseTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SubstanceAbuseTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SubstanceAbuseTemplate")

    id: Union[str, SubstanceAbuseTemplateId] = None
    stimulus: Optional[Union[str, MaterialEntityClassId]] = None
    stimulus_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubstanceAbuseTemplateId):
            self.id = SubstanceAbuseTemplateId(self.id)

        if self.stimulus is not None and not isinstance(self.stimulus, MaterialEntityClassId):
            self.stimulus = MaterialEntityClassId(self.stimulus)

        if self.stimulus_label is not None and not isinstance(self.stimulus_label, str):
            self.stimulus_label = str(self.stimulus_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class HemangiomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    A hemangioma (a benign vascular lesion characterized by the formation of capillary-sized or cavernous vascular
    channels) that is located in a specific anatomical site.
    Examples: [skin hemangioma](http://purl.obolibrary.org/obo/MONDO_0003110), [breast
    hemangioma](http://purl.obolibrary.org/obo/MONDO_0003126), [gastric
    hemangioma](http://purl.obolibrary.org/obo/MONDO_0002414) (20 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/HemangiomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "HemangiomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/HemangiomaDiseaseHasLocationXTemplate")

    id: Union[str, HemangiomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, AnatomicalEntityClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HemangiomaDiseaseHasLocationXTemplateId):
            self.id = HemangiomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, AnatomicalEntityClassId):
            self.location = AnatomicalEntityClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class ConsequenceOfInfectiousDiseaseTemplate(YAMLRoot):
    """
    This pattern is applied to a disease that is caused by an infectious agent.
    Examples: [hepatitis C induced liver cirrhosis](http://purl.obolibrary.org/obo/MONDO_0005448), [rubella
    encephalitis](http://purl.obolibrary.org/obo/MONDO_0020648)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ConsequenceOfInfectiousDiseaseTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ConsequenceOfInfectiousDiseaseTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ConsequenceOfInfectiousDiseaseTemplate")

    id: Union[str, ConsequenceOfInfectiousDiseaseTemplateId] = None
    parent: Optional[Union[str, DiseaseClassId]] = None
    parent_label: Optional[str] = None
    cause: Optional[Union[str, InfectiousDiseaseClassId]] = None
    cause_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsequenceOfInfectiousDiseaseTemplateId):
            self.id = ConsequenceOfInfectiousDiseaseTemplateId(self.id)

        if self.parent is not None and not isinstance(self.parent, DiseaseClassId):
            self.parent = DiseaseClassId(self.parent)

        if self.parent_label is not None and not isinstance(self.parent_label, str):
            self.parent_label = str(self.parent_label)

        if self.cause is not None and not isinstance(self.cause, InfectiousDiseaseClassId):
            self.cause = InfectiousDiseaseClassId(self.cause)

        if self.cause_label is not None and not isinstance(self.cause_label, str):
            self.cause_label = str(self.cause_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class InbornMetabolicTemplate(YAMLRoot):
    """
    An acquired metabolic disease that causes disruption of a process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InbornMetabolicTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "InbornMetabolicTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InbornMetabolicTemplate")

    id: Union[str, InbornMetabolicTemplateId] = None
    process: Optional[Union[str, ProcessClassId]] = None
    process_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InbornMetabolicTemplateId):
            self.id = InbornMetabolicTemplateId(self.id)

        if self.process is not None and not isinstance(self.process, ProcessClassId):
            self.process = ProcessClassId(self.process)

        if self.process_label is not None and not isinstance(self.process_label, str):
            self.process_label = str(self.process_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class MalignantTemplate(YAMLRoot):
    """
    This is a design pattern for classes representing malignant neoplasms, extending a generic neoplasm class.
    Examples: [malignant carotid body paraganglioma](http://purl.obolibrary.org/obo/MONDO_0004650), [malignant germ
    cell tumor](http://purl.obolibrary.org/obo/MONDO_0006290)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MalignantTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MalignantTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MalignantTemplate")

    id: Union[str, MalignantTemplateId] = None
    neoplasm: Optional[Union[str, OwlThingClassId]] = None
    neoplasm_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MalignantTemplateId):
            self.id = MalignantTemplateId(self.id)

        if self.neoplasm is not None and not isinstance(self.neoplasm, OwlThingClassId):
            self.neoplasm = OwlThingClassId(self.neoplasm)

        if self.neoplasm_label is not None and not isinstance(self.neoplasm_label, str):
            self.neoplasm_label = str(self.neoplasm_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AllergyTemplate(YAMLRoot):
    """
    Allergy classified according to allergic trigger. This pattern is to refine an existing disease by trigger, the
    [allergic_form_of_disease.yaml](https://github.com/monarch-initiative/mondo/blob/master/src/patterns/dosdp-patterns/allergic_form_of_disease.yaml)
    pattern is for a generic disease.
    Examples: [egg allergy](http://purl.obolibrary.org/obo/MONDO_0005741), [peach
    allergy](http://purl.obolibrary.org/obo/MONDO_0000785), [gluten
    allergy](http://purl.obolibrary.org/obo/MONDO_0000606)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AllergyTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AllergyTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AllergyTemplate")

    id: Union[str, AllergyTemplateId] = None
    substance: Optional[Union[str, OwlThingClassId]] = None
    substance_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AllergyTemplateId):
            self.id = AllergyTemplateId(self.id)

        if self.substance is not None and not isinstance(self.substance, OwlThingClassId):
            self.substance = OwlThingClassId(self.substance)

        if self.substance_label is not None and not isinstance(self.substance_label, str):
            self.substance_label = str(self.substance_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class MitochondriaalSubtypeTemplate(YAMLRoot):
    """
    A disease that is classified as a mitochondrial subtype, due to a defect in a mitochondrial gene, such as
    MONDO:0100134 'mitochondrial complex I deficiency, mitochondrial type'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MitochondriaalSubtypeTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MitochondriaalSubtypeTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MitochondriaalSubtypeTemplate")

    id: Union[str, MitochondriaalSubtypeTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MitochondriaalSubtypeTemplateId):
            self.id = MitochondriaalSubtypeTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class InfectiousInflammationTemplate(YAMLRoot):
    """
    This combines the [infectious disease by agent
    pattern](https://github.com/monarch-initiative/mondo/blob/master/src/patterns/dosdp-patterns/infectious_disease_by_agent.yaml)
    and the [inflammatory disease by
    site](https://github.com/monarch-initiative/mondo/blob/master/src/patterns/dosdp-patterns/inflammatory_disease_by_site.yaml)
    pattern.
    Examples: [bacterial endocarditis (disease)](http://purl.obolibrary.org/obo/MONDO_0006669), [fungal
    gastritis](http://purl.obolibrary.org/obo/MONDO_0002843)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InfectiousInflammationTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "InfectiousInflammationTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/InfectiousInflammationTemplate")

    id: Union[str, InfectiousInflammationTemplateId] = None
    location: Optional[Union[str, AnatomicalStructureClassId]] = None
    location_label: Optional[str] = None
    agent: Optional[Union[str, OrganismClassId]] = None
    agent_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InfectiousInflammationTemplateId):
            self.id = InfectiousInflammationTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, AnatomicalStructureClassId):
            self.location = AnatomicalStructureClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.agent is not None and not isinstance(self.agent, OrganismClassId):
            self.agent = OrganismClassId(self.agent)

        if self.agent_label is not None and not isinstance(self.agent_label, str):
            self.agent_label = str(self.agent_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class NeoplasmClass(YAMLRoot):
    """
    Any subclass of MONDO:0005070 ('neoplasm')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/NeoplasmClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NeoplasmClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/NeoplasmClass")

    id: Union[str, NeoplasmClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NeoplasmClassId):
            self.id = NeoplasmClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class BenignTemplate(YAMLRoot):
    """
    This is a design pattern for classes representing benign neoplasms, extending a generic neoplasm class. For
    example, a benign adrenal gland pheochromocytoma, defined as being the benign form of the more general adrenal
    gland pheochromocytoma.
    TODO: encode alternate way of representing
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/BenignTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BenignTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/BenignTemplate")

    id: Union[str, BenignTemplateId] = None
    neoplasm: Optional[Union[str, NeoplasmClassId]] = None
    neoplasm_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenignTemplateId):
            self.id = BenignTemplateId(self.id)

        if self.neoplasm is not None and not isinstance(self.neoplasm, NeoplasmClassId):
            self.neoplasm = NeoplasmClassId(self.neoplasm)

        if self.neoplasm_label is not None and not isinstance(self.neoplasm_label, str):
            self.neoplasm_label = str(self.neoplasm_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class MucoepidermoidCarcinomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    Mucoepidermoid carcinomas are carcinomas morphologically characterized the presence of cuboidal mucous cells,
    goblet-like mucous cells, squamoid cells, cystic changes, and a fibrotic stromal formation.
    This is a design pattern for classes representing mucoepidermoid carcinomas based on their location. This may be
    the site of origin, but it can also represent a secondary site for metastatized cancer.
    We use the generic 'disease has location' relation, which generalized over primary and secondary sites.
    Examples: [cutaneous mucoepidermoid carcinoma](http://purl.obolibrary.org/obo/MONDO_0003091), [oral cavity
    mucoepidermoid carcinoma](http://purl.obolibrary.org/obo/MONDO_0044964), [mucoepidermoid breast
    carcinoma](http://purl.obolibrary.org/obo/MONDO_0003087) (18 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MucoepidermoidCarcinomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MucoepidermoidCarcinomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MucoepidermoidCarcinomaDiseaseHasLocationXTemplate")

    id: Union[str, MucoepidermoidCarcinomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, AnatomicalEntityClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MucoepidermoidCarcinomaDiseaseHasLocationXTemplateId):
            self.id = MucoepidermoidCarcinomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, AnatomicalEntityClassId):
            self.location = AnatomicalEntityClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AutosomalDominantTemplate(YAMLRoot):
    """
    This pattern is applied to autosomal dominant forms of an inherited disease.
    Examples: [autosomal dominant cerebellar ataxia](http://purl.obolibrary.org/obo/MONDO_0020380), [autosomal
    dominant osteopetrosis](http://purl.obolibrary.org/obo/MONDO_0020645)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AutosomalDominantTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AutosomalDominantTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AutosomalDominantTemplate")

    id: Union[str, AutosomalDominantTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutosomalDominantTemplateId):
            self.id = AutosomalDominantTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class PrimaryInfectiousTemplate(YAMLRoot):
    """
    Pattern for extending a disease class to a primary infectious form, a characteristic of an infectious disease in
    which the disease affects an immunologically normal host. Example: MONDO_0000308 'primary systemic mycosis'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/PrimaryInfectiousTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PrimaryInfectiousTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/PrimaryInfectiousTemplate")

    id: Union[str, PrimaryInfectiousTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrimaryInfectiousTemplateId):
            self.id = PrimaryInfectiousTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class LymphomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    A malignant (clonal) proliferation of B- lymphocytes or T- lymphocytes which involves the lymph nodes, bone marrow
    and/or extranodal sites. This category includes Non-Hodgkin lymphomas and Hodgkin lymphomas.
    Examples: [marginal zone lymphoma](http://purl.obolibrary.org/obo/MONDO_0017604), [ureteral
    lymphoma](http://purl.obolibrary.org/obo/MONDO_0001977), [colorectal
    lymphoma](http://purl.obolibrary.org/obo/MONDO_0024656) (37 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LymphomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "LymphomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/LymphomaDiseaseHasLocationXTemplate")

    id: Union[str, LymphomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LymphomaDiseaseHasLocationXTemplateId):
            self.id = LymphomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class MulticellularAnatomicalStructureClass(YAMLRoot):
    """
    Any subclass of UBERON:0010000 ('multicellular anatomical structure')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MulticellularAnatomicalStructureClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MulticellularAnatomicalStructureClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/MulticellularAnatomicalStructureClass")

    id: Union[str, MulticellularAnatomicalStructureClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MulticellularAnatomicalStructureClassId):
            self.id = MulticellularAnatomicalStructureClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class AdenosquamousCarcinomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    An adenosquamous carcinoma is a carcinoma composed of malignant glandular cells and malignant squamous cells. This
    is a design pattern for classes representing adenosquamous carcinomas based on their location. This may be the
    site of origin, but it can also represent a secondary site for metastatized cancer. We use the generic 'disease
    has location' relation, which generalized over primary and secondary sites.
    Examples: [adenosquamous breast carcinoma](http://purl.obolibrary.org/obo/MONDO_0003548), [Bartholin gland
    adenosquamous carcinoma] (http://purl.obolibrary.org/obo/MONDO_0003555), [gastric adenosquamous
    carcinoma](http://purl.obolibrary.org/obo/MONDO_0006034)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AdenosquamousCarcinomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AdenosquamousCarcinomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AdenosquamousCarcinomaDiseaseHasLocationXTemplate")

    id: Union[str, AdenosquamousCarcinomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, MulticellularAnatomicalStructureClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdenosquamousCarcinomaDiseaseHasLocationXTemplateId):
            self.id = AdenosquamousCarcinomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, MulticellularAnatomicalStructureClassId):
            self.location = MulticellularAnatomicalStructureClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class XDiseaseDisruptsXTemplate(YAMLRoot):
    """
    This is auto-generated. Add your description here
    Examples: [disease of catalytic activity](http://purl.obolibrary.org/obo/MONDO_0044976), [disease of transporter
    activity](http://purl.obolibrary.org/obo/MONDO_0044975), [phagocytic cell
    dysfunction](http://purl.obolibrary.org/obo/MONDO_0024627) (49 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/XDiseaseDisruptsXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "XDiseaseDisruptsXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/XDiseaseDisruptsXTemplate")

    id: Union[str, XDiseaseDisruptsXTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    process: Optional[Union[str, OwlThingClassId]] = None
    process_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XDiseaseDisruptsXTemplateId):
            self.id = XDiseaseDisruptsXTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.process is not None and not isinstance(self.process, OwlThingClassId):
            self.process = OwlThingClassId(self.process)

        if self.process_label is not None and not isinstance(self.process_label, str):
            self.process_label = str(self.process_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class PoisoningTemplate(YAMLRoot):
    """
    A disease that is caused by exposure to an environmental stimulus that causes poisoning. Examples: [colchicine
    poisoning](http://purl.obolibrary.org/obo/MONDO_0017859), [cocaine
    intoxication](http://purl.obolibrary.org/obo/MONDO_0019544)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/PoisoningTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PoisoningTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/PoisoningTemplate")

    id: Union[str, PoisoningTemplateId] = None
    stimulus: Optional[Union[str, MaterialEntityClassId]] = None
    stimulus_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PoisoningTemplateId):
            self.id = PoisoningTemplateId(self.id)

        if self.stimulus is not None and not isinstance(self.stimulus, MaterialEntityClassId):
            self.stimulus = MaterialEntityClassId(self.stimulus)

        if self.stimulus_label is not None and not isinstance(self.stimulus_label, str):
            self.stimulus_label = str(self.stimulus_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class SusceptibilityByGeneTemplate(YAMLRoot):
    """
    This pattern should be used for terms in which a gene dysfunction causes a predisposition or susceptibility
    towards developing a specific disease. This pattern is a sub-pattern of
    [inherited_susceptibility.yaml](https://github.com/monarch-initiative/mondo/blob/master/src/patterns/dosdp-patterns/inherited_susceptibility.yaml)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SusceptibilityByGeneTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SusceptibilityByGeneTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SusceptibilityByGeneTemplate")

    id: Union[str, SusceptibilityByGeneTemplateId] = None
    gene: Optional[Union[str, GeneClassId]] = None
    gene_label: Optional[str] = None
    disease: Optional[Union[str, DiseaseOrDisorderClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SusceptibilityByGeneTemplateId):
            self.id = SusceptibilityByGeneTemplateId(self.id)

        if self.gene is not None and not isinstance(self.gene, GeneClassId):
            self.gene = GeneClassId(self.gene)

        if self.gene_label is not None and not isinstance(self.gene_label, str):
            self.gene_label = str(self.gene_label)

        if self.disease is not None and not isinstance(self.disease, DiseaseOrDisorderClassId):
            self.disease = DiseaseOrDisorderClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class OMIMDiseaseSeriesByGeneTemplate(YAMLRoot):
    """
    This pattern is meant to be used for OMIM diseases, including children of OMIM phenotypic series (OMIMPS), which
    are represented as grouping classes in Mondo. Notes about the OMIMPS (see also OMIM_phenotypic_series.yaml): -
    every instance of the OMIMPS metaclass should be equivalent to (via annotated xref) to something in OMIMPS
    namespace - the OMIMPS will never have an asserted causative gene as logical axiom (and no single causative gene
    in text def) - the OMIMPS must never be equivalent to an OMIM:nnnnnn (often redundant with the above rule) - the
    OMIMPS must have an acronym synonym, e.g. HPE - the OMIMPS must have two or more subclasses (direct or indirect)
    that are equivalent to OMIMs and conform to this pattern - the subclasses should (not must) have a logical def
    that uses the PS as a genus - the OMIM subclasses must have acronym synonyms that are the parent syn + number,
    e.g. HPE1, HPE2 - the primary label for the children should also be parent + {"type"} + number - the first member
    will usually have the same number local ID as the PS Examples: [holoprosencephaly
    1](http://purl.obolibrary.org/obo/MONDO_0009349), [3M syndrome 1](http://purl.obolibrary.org/obo/MONDO_0010117)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OMIMDiseaseSeriesByGeneTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OMIMDiseaseSeriesByGeneTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/OMIMDiseaseSeriesByGeneTemplate")

    id: Union[str, OMIMDiseaseSeriesByGeneTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    gene: Optional[Union[str, GeneClassId]] = None
    gene_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OMIMDiseaseSeriesByGeneTemplateId):
            self.id = OMIMDiseaseSeriesByGeneTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.gene is not None and not isinstance(self.gene, GeneClassId):
            self.gene = GeneClassId(self.gene)

        if self.gene_label is not None and not isinstance(self.gene_label, str):
            self.gene_label = str(self.gene_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AutoimmuneTemplate(YAMLRoot):
    """
    An instance of a disease that is brought about or caused by autoimmunity.
    Examples: [autoimmune cardiomyopathy](http://purl.obolibrary.org/obo/MONDO_0030701), [autoimmune
    pancreatitis](http://purl.obolibrary.org/obo/MONDO_0015175)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AutoimmuneTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AutoimmuneTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AutoimmuneTemplate")

    id: Union[str, AutoimmuneTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutoimmuneTemplateId):
            self.id = AutoimmuneTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AdenomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    Adenomas are neoplasms arising from epithelium. This is a design pattern for classes representing adenomas based
    on their location. This may be the site of origin, but it can also represent a secondary site for metastatized
    cancer. We use the generic `disease has location` relation, which is generalized over primary and secondary sites.
    Examples: [pituitary gland adenoma](http://purl.obolibrary.org/obo/MONDO_0006373), [breast
    adenoma](http://purl.obolibrary.org/obo/MONDO_0002058)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AdenomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AdenomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AdenomaDiseaseHasLocationXTemplate")

    id: Union[str, AdenomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdenomaDiseaseHasLocationXTemplateId):
            self.id = AdenomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class HereditaryTemplate(YAMLRoot):
    """
    Pattern for extending a etiology-generic disease class to a hereditary form. Here hereditary means that etiology
    is largely genetic, and that the disease is passed down or potentially able to be passed down via inheritance (i.e
    is germline).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/HereditaryTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "HereditaryTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/HereditaryTemplate")

    id: Union[str, HereditaryTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HereditaryTemplateId):
            self.id = HereditaryTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class JuvenileTemplate(YAMLRoot):
    """
    An instance of a disease that has an onset of signs or symptoms of disease between the age of 5 and 15 years
    (juvenile onset).
    Examples: [juvenile-onset Parkinson disease](http://purl.obolibrary.org/obo/MONDO_0000828), ['juvenile idiopathic
    scoliosis'](http://purl.obolibrary.org/obo/MONDO_0100076)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/JuvenileTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "JuvenileTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/JuvenileTemplate")

    id: Union[str, JuvenileTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JuvenileTemplateId):
            self.id = JuvenileTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class SquamousCellCarcinomaDiseaseHasLocationXTemplate(YAMLRoot):
    """
    This is auto-generated. Add your description here
    Examples: [cervical squamous cell carcinoma](http://purl.obolibrary.org/obo/MONDO_0006143), [skin squamous cell
    carcinoma](http://purl.obolibrary.org/obo/MONDO_0002529), [ureter squamous cell
    carcinoma](http://purl.obolibrary.org/obo/MONDO_0003502) (63 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SquamousCellCarcinomaDiseaseHasLocationXTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SquamousCellCarcinomaDiseaseHasLocationXTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SquamousCellCarcinomaDiseaseHasLocationXTemplate")

    id: Union[str, SquamousCellCarcinomaDiseaseHasLocationXTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SquamousCellCarcinomaDiseaseHasLocationXTemplateId):
            self.id = SquamousCellCarcinomaDiseaseHasLocationXTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventClass(YAMLRoot):
    """
    Any subclass of ExO:0000002 ('exposure event')
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ExposureEventClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExposureEventClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/ExposureEventClass")

    id: Union[str, ExposureEventClassId] = None
    subclass_of: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureEventClassId):
            self.id = ExposureEventClassId(self.id)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class DiseaseRealizedInResponseToEnvironmentalExposureTemplate(YAMLRoot):
    """
    This pattern is used for a disease, where the cause of the disease is an exposure to an environmental stimulus
    (using ECTO exposure terms). Note that this pattern does not include infectious disease or classes that would
    include an organism, virus or viroid. Rather it includes exposures to chemicals (includng drugs), or mixtures.
    Examples: [chemically-induced disorder](http://purl.obolibrary.org/obo/MONDO_0029001), [alcohol amnestic
    disorder](http://purl.obolibrary.org/obo/MONDO_0021702), [alcoholic
    polyneuropathy](http://purl.obolibrary.org/obo/MONDO_0006645) (26 total)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseRealizedInResponseToEnvironmentalExposureTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DiseaseRealizedInResponseToEnvironmentalExposureTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/DiseaseRealizedInResponseToEnvironmentalExposureTemplate")

    id: Union[str, DiseaseRealizedInResponseToEnvironmentalExposureTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    exposure: Optional[Union[str, ExposureEventClassId]] = None
    exposure_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseRealizedInResponseToEnvironmentalExposureTemplateId):
            self.id = DiseaseRealizedInResponseToEnvironmentalExposureTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.exposure is not None and not isinstance(self.exposure, ExposureEventClassId):
            self.exposure = ExposureEventClassId(self.exposure)

        if self.exposure_label is not None and not isinstance(self.exposure_label, str):
            self.exposure_label = str(self.exposure_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class SarcomaTemplate(YAMLRoot):
    """
    Sarcomas are malignant neoplasms arising from soft tissue or bone.
    This is a design pattern for classes representing sarcomas based on their location. This may be the site of
    origin, but it can also represent a secondary site for metastatized sarcma.
    We use the generic 'disease has location' relation, which generalized over primary and secondary sites.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SarcomaTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SarcomaTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SarcomaTemplate")

    id: Union[str, SarcomaTemplateId] = None
    location: Optional[Union[str, OwlThingClassId]] = None
    location_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SarcomaTemplateId):
            self.id = SarcomaTemplateId(self.id)

        if self.location is not None and not isinstance(self.location, OwlThingClassId):
            self.location = OwlThingClassId(self.location)

        if self.location_label is not None and not isinstance(self.location_label, str):
            self.location_label = str(self.location_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class SyndromicTemplate(YAMLRoot):
    """
    Some diseases exist in both isolated and syndromic forms. For example, aniridia ([MONDO_0019172
    aniridia](http://purl.obolibrary.org/obo/MONDO_0019172), [MONDO_0020148'syndromic
    aniridia'](http://purl.obolibrary.org/obo/MONDO_0020148) and [MONDO_0007119 'isolated
    aniridia'](http://purl.obolibrary.org/obo/MONDO_0007119). Use this pattern to define the syndromic form of a
    disease when a term exists for the isolated/syndromic-neutral version. In general, this pattern should be used in
    parallel with isolated. E.g. if you make a term 'syndromic disease, you should also have 'isolated disease' [see
    pattern here(https://github.com/monarch-initiative/mondo/blob/master/src/patterns/dosdp-patterns/isolated.yaml).
    Note that the isolated and syndromic forms will be inferred to be disjoint due to the GCI pattern.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SyndromicTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SyndromicTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/SyndromicTemplate")

    id: Union[str, SyndromicTemplateId] = None
    disease: Optional[Union[str, DiseaseOrDisorderClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SyndromicTemplateId):
            self.id = SyndromicTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseOrDisorderClassId):
            self.disease = DiseaseOrDisorderClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class AutosomalRecessiveTemplate(YAMLRoot):
    """
    This pattern is applied to autosomal recessive forms of an inherited disease.
    Examples: [autosomal recessive brachyolmia](http://purl.obolibrary.org/obo/MONDO_0018662), [autosomal recessive
    sideroblastic anemia](http://purl.obolibrary.org/obo/MONDO_0016828)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AutosomalRecessiveTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AutosomalRecessiveTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/AutosomalRecessiveTemplate")

    id: Union[str, AutosomalRecessiveTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutosomalRecessiveTemplateId):
            self.id = AutosomalRecessiveTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


@dataclass
class RefractoryTemplate(YAMLRoot):
    """
    TBD.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/RefractoryTemplate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "RefractoryTemplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/mondo/RefractoryTemplate")

    id: Union[str, RefractoryTemplateId] = None
    disease: Optional[Union[str, DiseaseClassId]] = None
    disease_label: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    equivalentTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RefractoryTemplateId):
            self.id = RefractoryTemplateId(self.id)

        if self.disease is not None and not isinstance(self.disease, DiseaseClassId):
            self.disease = DiseaseClassId(self.disease)

        if self.disease_label is not None and not isinstance(self.disease_label, str):
            self.disease_label = str(self.disease_label)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.equivalentTo is not None and not isinstance(self.equivalentTo, str):
            self.equivalentTo = str(self.equivalentTo)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

slots.definition = Slot(uri=IAO['0000115'], name="definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.definition, domain=None, range=Optional[str])

slots.subclass_of = Slot(uri=RDFS.subclass_of, name="subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.subclass_of, domain=None, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.equivalentTo, domain=None, range=Optional[str])

slots.location = Slot(uri=DEFAULT_.location, name="location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.location, domain=None, range=Optional[Union[str, OwlThingClassId]])

slots.location_label = Slot(uri=DEFAULT_.location_label, name="location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.location_label, domain=None, range=Optional[str])

slots.disease = Slot(uri=DEFAULT_.disease, name="disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.disease, domain=None, range=Optional[Union[str, DiseaseClassId]])

slots.disease_label = Slot(uri=DEFAULT_.disease_label, name="disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.disease_label, domain=None, range=Optional[str])

slots.stimulus = Slot(uri=DEFAULT_.stimulus, name="stimulus", curie=DEFAULT_.curie('stimulus'),
                   model_uri=DEFAULT_.stimulus, domain=None, range=Optional[Union[str, MaterialEntityClassId]])

slots.stimulus_label = Slot(uri=DEFAULT_.stimulus_label, name="stimulus_label", curie=DEFAULT_.curie('stimulus_label'),
                   model_uri=DEFAULT_.stimulus_label, domain=None, range=Optional[str])

slots.agent = Slot(uri=DEFAULT_.agent, name="agent", curie=DEFAULT_.curie('agent'),
                   model_uri=DEFAULT_.agent, domain=None, range=Optional[Union[str, OrganismClassId]])

slots.agent_label = Slot(uri=DEFAULT_.agent_label, name="agent_label", curie=DEFAULT_.curie('agent_label'),
                   model_uri=DEFAULT_.agent_label, domain=None, range=Optional[str])

slots.gene = Slot(uri=DEFAULT_.gene, name="gene", curie=DEFAULT_.curie('gene'),
                   model_uri=DEFAULT_.gene, domain=None, range=Optional[Union[str, GeneClassId]])

slots.gene_label = Slot(uri=DEFAULT_.gene_label, name="gene_label", curie=DEFAULT_.curie('gene_label'),
                   model_uri=DEFAULT_.gene_label, domain=None, range=Optional[str])

slots.mode_of_inheritance = Slot(uri=DEFAULT_.mode_of_inheritance, name="mode_of_inheritance", curie=DEFAULT_.curie('mode_of_inheritance'),
                   model_uri=DEFAULT_.mode_of_inheritance, domain=None, range=Optional[Union[str, ModeOfInheritanceClassId]])

slots.mode_of_inheritance_label = Slot(uri=DEFAULT_.mode_of_inheritance_label, name="mode_of_inheritance_label", curie=DEFAULT_.curie('mode_of_inheritance_label'),
                   model_uri=DEFAULT_.mode_of_inheritance_label, domain=None, range=Optional[str])

slots.structure = Slot(uri=DEFAULT_.structure, name="structure", curie=DEFAULT_.curie('structure'),
                   model_uri=DEFAULT_.structure, domain=None, range=Optional[Union[str, OwlThingClassId]])

slots.structure_label = Slot(uri=DEFAULT_.structure_label, name="structure_label", curie=DEFAULT_.curie('structure_label'),
                   model_uri=DEFAULT_.structure_label, domain=None, range=Optional[str])

slots.process = Slot(uri=DEFAULT_.process, name="process", curie=DEFAULT_.curie('process'),
                   model_uri=DEFAULT_.process, domain=None, range=Optional[Union[str, OwlThingClassId]])

slots.process_label = Slot(uri=DEFAULT_.process_label, name="process_label", curie=DEFAULT_.curie('process_label'),
                   model_uri=DEFAULT_.process_label, domain=None, range=Optional[str])

slots.feature = Slot(uri=DEFAULT_.feature, name="feature", curie=DEFAULT_.curie('feature'),
                   model_uri=DEFAULT_.feature, domain=None, range=Optional[Union[str, InfectiousDiseaseClassId]])

slots.feature_label = Slot(uri=DEFAULT_.feature_label, name="feature_label", curie=DEFAULT_.curie('feature_label'),
                   model_uri=DEFAULT_.feature_label, domain=None, range=Optional[str])

slots.infectious_disease = Slot(uri=DEFAULT_.infectious_disease, name="infectious_disease", curie=DEFAULT_.curie('infectious_disease'),
                   model_uri=DEFAULT_.infectious_disease, domain=None, range=Optional[Union[str, InfectiousDiseaseClassId]])

slots.infectious_disease_label = Slot(uri=DEFAULT_.infectious_disease_label, name="infectious_disease_label", curie=DEFAULT_.curie('infectious_disease_label'),
                   model_uri=DEFAULT_.infectious_disease_label, domain=None, range=Optional[str])

slots.vector = Slot(uri=DEFAULT_.vector, name="vector", curie=DEFAULT_.curie('vector'),
                   model_uri=DEFAULT_.vector, domain=None, range=Optional[Union[str, OrganismClassId]])

slots.vector_label = Slot(uri=DEFAULT_.vector_label, name="vector_label", curie=DEFAULT_.curie('vector_label'),
                   model_uri=DEFAULT_.vector_label, domain=None, range=Optional[str])

slots.parent = Slot(uri=DEFAULT_.parent, name="parent", curie=DEFAULT_.curie('parent'),
                   model_uri=DEFAULT_.parent, domain=None, range=Optional[Union[str, DiseaseClassId]])

slots.parent_label = Slot(uri=DEFAULT_.parent_label, name="parent_label", curie=DEFAULT_.curie('parent_label'),
                   model_uri=DEFAULT_.parent_label, domain=None, range=Optional[str])

slots.cause = Slot(uri=DEFAULT_.cause, name="cause", curie=DEFAULT_.curie('cause'),
                   model_uri=DEFAULT_.cause, domain=None, range=Optional[Union[str, InfectiousDiseaseClassId]])

slots.cause_label = Slot(uri=DEFAULT_.cause_label, name="cause_label", curie=DEFAULT_.curie('cause_label'),
                   model_uri=DEFAULT_.cause_label, domain=None, range=Optional[str])

slots.neoplasm = Slot(uri=DEFAULT_.neoplasm, name="neoplasm", curie=DEFAULT_.curie('neoplasm'),
                   model_uri=DEFAULT_.neoplasm, domain=None, range=Optional[Union[str, NeoplasmClassId]])

slots.neoplasm_label = Slot(uri=DEFAULT_.neoplasm_label, name="neoplasm_label", curie=DEFAULT_.curie('neoplasm_label'),
                   model_uri=DEFAULT_.neoplasm_label, domain=None, range=Optional[str])

slots.substance = Slot(uri=DEFAULT_.substance, name="substance", curie=DEFAULT_.curie('substance'),
                   model_uri=DEFAULT_.substance, domain=None, range=Optional[Union[str, OwlThingClassId]])

slots.substance_label = Slot(uri=DEFAULT_.substance_label, name="substance_label", curie=DEFAULT_.curie('substance_label'),
                   model_uri=DEFAULT_.substance_label, domain=None, range=Optional[str])

slots.exposure = Slot(uri=DEFAULT_.exposure, name="exposure", curie=DEFAULT_.curie('exposure'),
                   model_uri=DEFAULT_.exposure, domain=None, range=Optional[Union[str, ExposureEventClassId]])

slots.exposure_label = Slot(uri=DEFAULT_.exposure_label, name="exposure_label", curie=DEFAULT_.curie('exposure_label'),
                   model_uri=DEFAULT_.exposure_label, domain=None, range=Optional[str])

slots.OwlThingClass_subclass_of = Slot(uri=RDFS.subclass_of, name="OwlThingClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.OwlThingClass_subclass_of, domain=OwlThingClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.LocationTopTemplate_location = Slot(uri=DEFAULT_.location, name="LocationTopTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.LocationTopTemplate_location, domain=LocationTopTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.LocationTopTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="LocationTopTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.LocationTopTemplate_location_label, domain=LocationTopTemplate, range=Optional[str])

slots.LocationTopTemplate_name = Slot(uri=RDFS.label, name="LocationTopTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.LocationTopTemplate_name, domain=LocationTopTemplate, range=Optional[str])

slots.LocationTopTemplate_definition = Slot(uri=IAO['0000115'], name="LocationTopTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.LocationTopTemplate_definition, domain=LocationTopTemplate, range=Optional[str])

slots.LocationTopTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="LocationTopTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.LocationTopTemplate_equivalentTo, domain=LocationTopTemplate, range=Optional[str])

slots.DiseaseClass_subclass_of = Slot(uri=RDFS.subclass_of, name="DiseaseClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.DiseaseClass_subclass_of, domain=DiseaseClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.MaterialEntityClass_subclass_of = Slot(uri=RDFS.subclass_of, name="MaterialEntityClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.MaterialEntityClass_subclass_of, domain=MaterialEntityClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.EnvironmentalStimulusTemplate_disease = Slot(uri=DEFAULT_.disease, name="EnvironmentalStimulusTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.EnvironmentalStimulusTemplate_disease, domain=EnvironmentalStimulusTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.EnvironmentalStimulusTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="EnvironmentalStimulusTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.EnvironmentalStimulusTemplate_disease_label, domain=EnvironmentalStimulusTemplate, range=Optional[str])

slots.EnvironmentalStimulusTemplate_stimulus = Slot(uri=DEFAULT_.stimulus, name="EnvironmentalStimulusTemplate_stimulus", curie=DEFAULT_.curie('stimulus'),
                   model_uri=DEFAULT_.EnvironmentalStimulusTemplate_stimulus, domain=EnvironmentalStimulusTemplate, range=Optional[Union[str, MaterialEntityClassId]])

slots.EnvironmentalStimulusTemplate_stimulus_label = Slot(uri=DEFAULT_.stimulus_label, name="EnvironmentalStimulusTemplate_stimulus_label", curie=DEFAULT_.curie('stimulus_label'),
                   model_uri=DEFAULT_.EnvironmentalStimulusTemplate_stimulus_label, domain=EnvironmentalStimulusTemplate, range=Optional[str])

slots.EnvironmentalStimulusTemplate_name = Slot(uri=RDFS.label, name="EnvironmentalStimulusTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.EnvironmentalStimulusTemplate_name, domain=EnvironmentalStimulusTemplate, range=Optional[str])

slots.EnvironmentalStimulusTemplate_definition = Slot(uri=IAO['0000115'], name="EnvironmentalStimulusTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.EnvironmentalStimulusTemplate_definition, domain=EnvironmentalStimulusTemplate, range=Optional[str])

slots.EnvironmentalStimulusTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="EnvironmentalStimulusTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.EnvironmentalStimulusTemplate_equivalentTo, domain=EnvironmentalStimulusTemplate, range=Optional[str])

slots.AnatomicalStructureClass_subclass_of = Slot(uri=RDFS.subclass_of, name="AnatomicalStructureClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.AnatomicalStructureClass_subclass_of, domain=AnatomicalStructureClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.SpecificInfectiousDiseaseByLocationTemplate_disease = Slot(uri=DEFAULT_.disease, name="SpecificInfectiousDiseaseByLocationTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.SpecificInfectiousDiseaseByLocationTemplate_disease, domain=SpecificInfectiousDiseaseByLocationTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.SpecificInfectiousDiseaseByLocationTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="SpecificInfectiousDiseaseByLocationTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.SpecificInfectiousDiseaseByLocationTemplate_disease_label, domain=SpecificInfectiousDiseaseByLocationTemplate, range=Optional[str])

slots.SpecificInfectiousDiseaseByLocationTemplate_location = Slot(uri=DEFAULT_.location, name="SpecificInfectiousDiseaseByLocationTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.SpecificInfectiousDiseaseByLocationTemplate_location, domain=SpecificInfectiousDiseaseByLocationTemplate, range=Optional[Union[str, AnatomicalStructureClassId]])

slots.SpecificInfectiousDiseaseByLocationTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="SpecificInfectiousDiseaseByLocationTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.SpecificInfectiousDiseaseByLocationTemplate_location_label, domain=SpecificInfectiousDiseaseByLocationTemplate, range=Optional[str])

slots.SpecificInfectiousDiseaseByLocationTemplate_name = Slot(uri=RDFS.label, name="SpecificInfectiousDiseaseByLocationTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.SpecificInfectiousDiseaseByLocationTemplate_name, domain=SpecificInfectiousDiseaseByLocationTemplate, range=Optional[str])

slots.SpecificInfectiousDiseaseByLocationTemplate_definition = Slot(uri=IAO['0000115'], name="SpecificInfectiousDiseaseByLocationTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.SpecificInfectiousDiseaseByLocationTemplate_definition, domain=SpecificInfectiousDiseaseByLocationTemplate, range=Optional[str])

slots.SpecificInfectiousDiseaseByLocationTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="SpecificInfectiousDiseaseByLocationTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.SpecificInfectiousDiseaseByLocationTemplate_equivalentTo, domain=SpecificInfectiousDiseaseByLocationTemplate, range=Optional[str])

slots.AutoimmuneInflammationTemplate_location = Slot(uri=DEFAULT_.location, name="AutoimmuneInflammationTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.AutoimmuneInflammationTemplate_location, domain=AutoimmuneInflammationTemplate, range=Optional[Union[str, AnatomicalStructureClassId]])

slots.AutoimmuneInflammationTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="AutoimmuneInflammationTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.AutoimmuneInflammationTemplate_location_label, domain=AutoimmuneInflammationTemplate, range=Optional[str])

slots.AutoimmuneInflammationTemplate_name = Slot(uri=RDFS.label, name="AutoimmuneInflammationTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AutoimmuneInflammationTemplate_name, domain=AutoimmuneInflammationTemplate, range=Optional[str])

slots.AutoimmuneInflammationTemplate_definition = Slot(uri=IAO['0000115'], name="AutoimmuneInflammationTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AutoimmuneInflammationTemplate_definition, domain=AutoimmuneInflammationTemplate, range=Optional[str])

slots.AutoimmuneInflammationTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AutoimmuneInflammationTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AutoimmuneInflammationTemplate_equivalentTo, domain=AutoimmuneInflammationTemplate, range=Optional[str])

slots.AcquiredTemplate_disease = Slot(uri=DEFAULT_.disease, name="AcquiredTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.AcquiredTemplate_disease, domain=AcquiredTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.AcquiredTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="AcquiredTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.AcquiredTemplate_disease_label, domain=AcquiredTemplate, range=Optional[str])

slots.AcquiredTemplate_name = Slot(uri=RDFS.label, name="AcquiredTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AcquiredTemplate_name, domain=AcquiredTemplate, range=Optional[str])

slots.AcquiredTemplate_definition = Slot(uri=IAO['0000115'], name="AcquiredTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AcquiredTemplate_definition, domain=AcquiredTemplate, range=Optional[str])

slots.AcquiredTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AcquiredTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AcquiredTemplate_equivalentTo, domain=AcquiredTemplate, range=Optional[str])

slots.CarcinomaInSituTemplate_location = Slot(uri=DEFAULT_.location, name="CarcinomaInSituTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.CarcinomaInSituTemplate_location, domain=CarcinomaInSituTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.CarcinomaInSituTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="CarcinomaInSituTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.CarcinomaInSituTemplate_location_label, domain=CarcinomaInSituTemplate, range=Optional[str])

slots.CarcinomaInSituTemplate_name = Slot(uri=RDFS.label, name="CarcinomaInSituTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.CarcinomaInSituTemplate_name, domain=CarcinomaInSituTemplate, range=Optional[str])

slots.CarcinomaInSituTemplate_definition = Slot(uri=IAO['0000115'], name="CarcinomaInSituTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.CarcinomaInSituTemplate_definition, domain=CarcinomaInSituTemplate, range=Optional[str])

slots.CarcinomaInSituTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="CarcinomaInSituTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.CarcinomaInSituTemplate_equivalentTo, domain=CarcinomaInSituTemplate, range=Optional[str])

slots.AllergicFormOfDiseaseTemplate_disease = Slot(uri=DEFAULT_.disease, name="AllergicFormOfDiseaseTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.AllergicFormOfDiseaseTemplate_disease, domain=AllergicFormOfDiseaseTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.AllergicFormOfDiseaseTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="AllergicFormOfDiseaseTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.AllergicFormOfDiseaseTemplate_disease_label, domain=AllergicFormOfDiseaseTemplate, range=Optional[str])

slots.AllergicFormOfDiseaseTemplate_name = Slot(uri=RDFS.label, name="AllergicFormOfDiseaseTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AllergicFormOfDiseaseTemplate_name, domain=AllergicFormOfDiseaseTemplate, range=Optional[str])

slots.AllergicFormOfDiseaseTemplate_definition = Slot(uri=IAO['0000115'], name="AllergicFormOfDiseaseTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AllergicFormOfDiseaseTemplate_definition, domain=AllergicFormOfDiseaseTemplate, range=Optional[str])

slots.AllergicFormOfDiseaseTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AllergicFormOfDiseaseTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AllergicFormOfDiseaseTemplate_equivalentTo, domain=AllergicFormOfDiseaseTemplate, range=Optional[str])

slots.AcuteTemplate_disease = Slot(uri=DEFAULT_.disease, name="AcuteTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.AcuteTemplate_disease, domain=AcuteTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.AcuteTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="AcuteTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.AcuteTemplate_disease_label, domain=AcuteTemplate, range=Optional[str])

slots.AcuteTemplate_name = Slot(uri=RDFS.label, name="AcuteTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AcuteTemplate_name, domain=AcuteTemplate, range=Optional[str])

slots.AcuteTemplate_definition = Slot(uri=IAO['0000115'], name="AcuteTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AcuteTemplate_definition, domain=AcuteTemplate, range=Optional[str])

slots.AcuteTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AcuteTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AcuteTemplate_equivalentTo, domain=AcuteTemplate, range=Optional[str])

slots.NuclearSubtypeTemplate_disease = Slot(uri=DEFAULT_.disease, name="NuclearSubtypeTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.NuclearSubtypeTemplate_disease, domain=NuclearSubtypeTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.NuclearSubtypeTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="NuclearSubtypeTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.NuclearSubtypeTemplate_disease_label, domain=NuclearSubtypeTemplate, range=Optional[str])

slots.NuclearSubtypeTemplate_name = Slot(uri=RDFS.label, name="NuclearSubtypeTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.NuclearSubtypeTemplate_name, domain=NuclearSubtypeTemplate, range=Optional[str])

slots.NuclearSubtypeTemplate_definition = Slot(uri=IAO['0000115'], name="NuclearSubtypeTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.NuclearSubtypeTemplate_definition, domain=NuclearSubtypeTemplate, range=Optional[str])

slots.NuclearSubtypeTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="NuclearSubtypeTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.NuclearSubtypeTemplate_equivalentTo, domain=NuclearSubtypeTemplate, range=Optional[str])

slots.InfantileTemplate_disease = Slot(uri=DEFAULT_.disease, name="InfantileTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.InfantileTemplate_disease, domain=InfantileTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.InfantileTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="InfantileTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.InfantileTemplate_disease_label, domain=InfantileTemplate, range=Optional[str])

slots.InfantileTemplate_name = Slot(uri=RDFS.label, name="InfantileTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.InfantileTemplate_name, domain=InfantileTemplate, range=Optional[str])

slots.InfantileTemplate_definition = Slot(uri=IAO['0000115'], name="InfantileTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.InfantileTemplate_definition, domain=InfantileTemplate, range=Optional[str])

slots.InfantileTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="InfantileTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.InfantileTemplate_equivalentTo, domain=InfantileTemplate, range=Optional[str])

slots.XLinkedTemplate_disease = Slot(uri=DEFAULT_.disease, name="XLinkedTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.XLinkedTemplate_disease, domain=XLinkedTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.XLinkedTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="XLinkedTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.XLinkedTemplate_disease_label, domain=XLinkedTemplate, range=Optional[str])

slots.XLinkedTemplate_name = Slot(uri=RDFS.label, name="XLinkedTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.XLinkedTemplate_name, domain=XLinkedTemplate, range=Optional[str])

slots.XLinkedTemplate_definition = Slot(uri=IAO['0000115'], name="XLinkedTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.XLinkedTemplate_definition, domain=XLinkedTemplate, range=Optional[str])

slots.XLinkedTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="XLinkedTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.XLinkedTemplate_equivalentTo, domain=XLinkedTemplate, range=Optional[str])

slots.IdiopathicTemplate_disease = Slot(uri=DEFAULT_.disease, name="IdiopathicTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.IdiopathicTemplate_disease, domain=IdiopathicTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.IdiopathicTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="IdiopathicTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.IdiopathicTemplate_disease_label, domain=IdiopathicTemplate, range=Optional[str])

slots.IdiopathicTemplate_name = Slot(uri=RDFS.label, name="IdiopathicTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.IdiopathicTemplate_name, domain=IdiopathicTemplate, range=Optional[str])

slots.IdiopathicTemplate_definition = Slot(uri=IAO['0000115'], name="IdiopathicTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.IdiopathicTemplate_definition, domain=IdiopathicTemplate, range=Optional[str])

slots.IdiopathicTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="IdiopathicTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.IdiopathicTemplate_equivalentTo, domain=IdiopathicTemplate, range=Optional[str])

slots.ChronicTemplate_disease = Slot(uri=DEFAULT_.disease, name="ChronicTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.ChronicTemplate_disease, domain=ChronicTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.ChronicTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="ChronicTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.ChronicTemplate_disease_label, domain=ChronicTemplate, range=Optional[str])

slots.ChronicTemplate_name = Slot(uri=RDFS.label, name="ChronicTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.ChronicTemplate_name, domain=ChronicTemplate, range=Optional[str])

slots.ChronicTemplate_definition = Slot(uri=IAO['0000115'], name="ChronicTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.ChronicTemplate_definition, domain=ChronicTemplate, range=Optional[str])

slots.ChronicTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="ChronicTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.ChronicTemplate_equivalentTo, domain=ChronicTemplate, range=Optional[str])

slots.MelanomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="MelanomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.MelanomaDiseaseHasLocationXTemplate_location, domain=MelanomaDiseaseHasLocationXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.MelanomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="MelanomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.MelanomaDiseaseHasLocationXTemplate_location_label, domain=MelanomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.MelanomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="MelanomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.MelanomaDiseaseHasLocationXTemplate_name, domain=MelanomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.MelanomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="MelanomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.MelanomaDiseaseHasLocationXTemplate_definition, domain=MelanomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.MelanomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="MelanomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.MelanomaDiseaseHasLocationXTemplate_equivalentTo, domain=MelanomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.SpecificInflammatoryDiseaseBySiteTemplate_disease = Slot(uri=DEFAULT_.disease, name="SpecificInflammatoryDiseaseBySiteTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.SpecificInflammatoryDiseaseBySiteTemplate_disease, domain=SpecificInflammatoryDiseaseBySiteTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.SpecificInflammatoryDiseaseBySiteTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="SpecificInflammatoryDiseaseBySiteTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.SpecificInflammatoryDiseaseBySiteTemplate_disease_label, domain=SpecificInflammatoryDiseaseBySiteTemplate, range=Optional[str])

slots.SpecificInflammatoryDiseaseBySiteTemplate_agent = Slot(uri=DEFAULT_.agent, name="SpecificInflammatoryDiseaseBySiteTemplate_agent", curie=DEFAULT_.curie('agent'),
                   model_uri=DEFAULT_.SpecificInflammatoryDiseaseBySiteTemplate_agent, domain=SpecificInflammatoryDiseaseBySiteTemplate, range=Optional[Union[str, OrganismClassId]])

slots.SpecificInflammatoryDiseaseBySiteTemplate_agent_label = Slot(uri=DEFAULT_.agent_label, name="SpecificInflammatoryDiseaseBySiteTemplate_agent_label", curie=DEFAULT_.curie('agent_label'),
                   model_uri=DEFAULT_.SpecificInflammatoryDiseaseBySiteTemplate_agent_label, domain=SpecificInflammatoryDiseaseBySiteTemplate, range=Optional[str])

slots.SpecificInflammatoryDiseaseBySiteTemplate_name = Slot(uri=RDFS.label, name="SpecificInflammatoryDiseaseBySiteTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.SpecificInflammatoryDiseaseBySiteTemplate_name, domain=SpecificInflammatoryDiseaseBySiteTemplate, range=Optional[str])

slots.SpecificInflammatoryDiseaseBySiteTemplate_definition = Slot(uri=IAO['0000115'], name="SpecificInflammatoryDiseaseBySiteTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.SpecificInflammatoryDiseaseBySiteTemplate_definition, domain=SpecificInflammatoryDiseaseBySiteTemplate, range=Optional[str])

slots.SpecificInflammatoryDiseaseBySiteTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="SpecificInflammatoryDiseaseBySiteTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.SpecificInflammatoryDiseaseBySiteTemplate_equivalentTo, domain=SpecificInflammatoryDiseaseBySiteTemplate, range=Optional[str])

slots.SmallCellCarcinomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="SmallCellCarcinomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.SmallCellCarcinomaDiseaseHasLocationXTemplate_location, domain=SmallCellCarcinomaDiseaseHasLocationXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.SmallCellCarcinomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="SmallCellCarcinomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.SmallCellCarcinomaDiseaseHasLocationXTemplate_location_label, domain=SmallCellCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.SmallCellCarcinomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="SmallCellCarcinomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.SmallCellCarcinomaDiseaseHasLocationXTemplate_name, domain=SmallCellCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.SmallCellCarcinomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="SmallCellCarcinomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.SmallCellCarcinomaDiseaseHasLocationXTemplate_definition, domain=SmallCellCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.SmallCellCarcinomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="SmallCellCarcinomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.SmallCellCarcinomaDiseaseHasLocationXTemplate_equivalentTo, domain=SmallCellCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.RareTemplate_disease = Slot(uri=DEFAULT_.disease, name="RareTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.RareTemplate_disease, domain=RareTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.RareTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="RareTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.RareTemplate_disease_label, domain=RareTemplate, range=Optional[str])

slots.RareTemplate_name = Slot(uri=RDFS.label, name="RareTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.RareTemplate_name, domain=RareTemplate, range=Optional[str])

slots.RareTemplate_definition = Slot(uri=IAO['0000115'], name="RareTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.RareTemplate_definition, domain=RareTemplate, range=Optional[str])

slots.RareTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="RareTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.RareTemplate_equivalentTo, domain=RareTemplate, range=Optional[str])

slots.GeneticTemplate_disease = Slot(uri=DEFAULT_.disease, name="GeneticTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.GeneticTemplate_disease, domain=GeneticTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.GeneticTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="GeneticTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.GeneticTemplate_disease_label, domain=GeneticTemplate, range=Optional[str])

slots.GeneticTemplate_name = Slot(uri=RDFS.label, name="GeneticTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.GeneticTemplate_name, domain=GeneticTemplate, range=Optional[str])

slots.GeneticTemplate_definition = Slot(uri=IAO['0000115'], name="GeneticTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.GeneticTemplate_definition, domain=GeneticTemplate, range=Optional[str])

slots.GeneticTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="GeneticTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.GeneticTemplate_equivalentTo, domain=GeneticTemplate, range=Optional[str])

slots.OrganismClass_subclass_of = Slot(uri=RDFS.subclass_of, name="OrganismClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.OrganismClass_subclass_of, domain=OrganismClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.GeneClass_subclass_of = Slot(uri=RDFS.subclass_of, name="GeneClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.GeneClass_subclass_of, domain=GeneClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.ModeOfInheritanceClass_subclass_of = Slot(uri=RDFS.subclass_of, name="ModeOfInheritanceClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.ModeOfInheritanceClass_subclass_of, domain=ModeOfInheritanceClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.DiseaseSeriesByGeneAndInheritanceTemplate_disease = Slot(uri=DEFAULT_.disease, name="DiseaseSeriesByGeneAndInheritanceTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneAndInheritanceTemplate_disease, domain=DiseaseSeriesByGeneAndInheritanceTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.DiseaseSeriesByGeneAndInheritanceTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="DiseaseSeriesByGeneAndInheritanceTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneAndInheritanceTemplate_disease_label, domain=DiseaseSeriesByGeneAndInheritanceTemplate, range=Optional[str])

slots.DiseaseSeriesByGeneAndInheritanceTemplate_gene = Slot(uri=DEFAULT_.gene, name="DiseaseSeriesByGeneAndInheritanceTemplate_gene", curie=DEFAULT_.curie('gene'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneAndInheritanceTemplate_gene, domain=DiseaseSeriesByGeneAndInheritanceTemplate, range=Optional[Union[str, GeneClassId]])

slots.DiseaseSeriesByGeneAndInheritanceTemplate_gene_label = Slot(uri=DEFAULT_.gene_label, name="DiseaseSeriesByGeneAndInheritanceTemplate_gene_label", curie=DEFAULT_.curie('gene_label'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneAndInheritanceTemplate_gene_label, domain=DiseaseSeriesByGeneAndInheritanceTemplate, range=Optional[str])

slots.DiseaseSeriesByGeneAndInheritanceTemplate_mode_of_inheritance = Slot(uri=DEFAULT_.mode_of_inheritance, name="DiseaseSeriesByGeneAndInheritanceTemplate_mode_of_inheritance", curie=DEFAULT_.curie('mode_of_inheritance'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneAndInheritanceTemplate_mode_of_inheritance, domain=DiseaseSeriesByGeneAndInheritanceTemplate, range=Optional[Union[str, ModeOfInheritanceClassId]])

slots.DiseaseSeriesByGeneAndInheritanceTemplate_mode_of_inheritance_label = Slot(uri=DEFAULT_.mode_of_inheritance_label, name="DiseaseSeriesByGeneAndInheritanceTemplate_mode_of_inheritance_label", curie=DEFAULT_.curie('mode_of_inheritance_label'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneAndInheritanceTemplate_mode_of_inheritance_label, domain=DiseaseSeriesByGeneAndInheritanceTemplate, range=Optional[str])

slots.DiseaseSeriesByGeneAndInheritanceTemplate_name = Slot(uri=RDFS.label, name="DiseaseSeriesByGeneAndInheritanceTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneAndInheritanceTemplate_name, domain=DiseaseSeriesByGeneAndInheritanceTemplate, range=Optional[str])

slots.DiseaseSeriesByGeneAndInheritanceTemplate_definition = Slot(uri=IAO['0000115'], name="DiseaseSeriesByGeneAndInheritanceTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneAndInheritanceTemplate_definition, domain=DiseaseSeriesByGeneAndInheritanceTemplate, range=Optional[str])

slots.DiseaseSeriesByGeneAndInheritanceTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="DiseaseSeriesByGeneAndInheritanceTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneAndInheritanceTemplate_equivalentTo, domain=DiseaseSeriesByGeneAndInheritanceTemplate, range=Optional[str])

slots.DiseaseByDysfunctionalStructureTemplate_structure = Slot(uri=DEFAULT_.structure, name="DiseaseByDysfunctionalStructureTemplate_structure", curie=DEFAULT_.curie('structure'),
                   model_uri=DEFAULT_.DiseaseByDysfunctionalStructureTemplate_structure, domain=DiseaseByDysfunctionalStructureTemplate, range=Optional[Union[str, AnatomicalStructureClassId]])

slots.DiseaseByDysfunctionalStructureTemplate_structure_label = Slot(uri=DEFAULT_.structure_label, name="DiseaseByDysfunctionalStructureTemplate_structure_label", curie=DEFAULT_.curie('structure_label'),
                   model_uri=DEFAULT_.DiseaseByDysfunctionalStructureTemplate_structure_label, domain=DiseaseByDysfunctionalStructureTemplate, range=Optional[str])

slots.DiseaseByDysfunctionalStructureTemplate_name = Slot(uri=RDFS.label, name="DiseaseByDysfunctionalStructureTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.DiseaseByDysfunctionalStructureTemplate_name, domain=DiseaseByDysfunctionalStructureTemplate, range=Optional[str])

slots.DiseaseByDysfunctionalStructureTemplate_definition = Slot(uri=IAO['0000115'], name="DiseaseByDysfunctionalStructureTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.DiseaseByDysfunctionalStructureTemplate_definition, domain=DiseaseByDysfunctionalStructureTemplate, range=Optional[str])

slots.DiseaseByDysfunctionalStructureTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="DiseaseByDysfunctionalStructureTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.DiseaseByDysfunctionalStructureTemplate_equivalentTo, domain=DiseaseByDysfunctionalStructureTemplate, range=Optional[str])

slots.NeoplasmTemplate_structure = Slot(uri=DEFAULT_.structure, name="NeoplasmTemplate_structure", curie=DEFAULT_.curie('structure'),
                   model_uri=DEFAULT_.NeoplasmTemplate_structure, domain=NeoplasmTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.NeoplasmTemplate_structure_label = Slot(uri=DEFAULT_.structure_label, name="NeoplasmTemplate_structure_label", curie=DEFAULT_.curie('structure_label'),
                   model_uri=DEFAULT_.NeoplasmTemplate_structure_label, domain=NeoplasmTemplate, range=Optional[str])

slots.NeoplasmTemplate_name = Slot(uri=RDFS.label, name="NeoplasmTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.NeoplasmTemplate_name, domain=NeoplasmTemplate, range=Optional[str])

slots.NeoplasmTemplate_definition = Slot(uri=IAO['0000115'], name="NeoplasmTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.NeoplasmTemplate_definition, domain=NeoplasmTemplate, range=Optional[str])

slots.NeoplasmTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="NeoplasmTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.NeoplasmTemplate_equivalentTo, domain=NeoplasmTemplate, range=Optional[str])

slots.IsolatedTemplate_disease = Slot(uri=DEFAULT_.disease, name="IsolatedTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.IsolatedTemplate_disease, domain=IsolatedTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.IsolatedTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="IsolatedTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.IsolatedTemplate_disease_label, domain=IsolatedTemplate, range=Optional[str])

slots.IsolatedTemplate_name = Slot(uri=RDFS.label, name="IsolatedTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.IsolatedTemplate_name, domain=IsolatedTemplate, range=Optional[str])

slots.IsolatedTemplate_definition = Slot(uri=IAO['0000115'], name="IsolatedTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.IsolatedTemplate_definition, domain=IsolatedTemplate, range=Optional[str])

slots.IsolatedTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="IsolatedTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.IsolatedTemplate_equivalentTo, domain=IsolatedTemplate, range=Optional[str])

slots.ChemicalClass_subclass_of = Slot(uri=RDFS.subclass_of, name="ChemicalClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.ChemicalClass_subclass_of, domain=ChemicalClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.DependenceOnSubstanceTemplate_stimulus = Slot(uri=DEFAULT_.stimulus, name="DependenceOnSubstanceTemplate_stimulus", curie=DEFAULT_.curie('stimulus'),
                   model_uri=DEFAULT_.DependenceOnSubstanceTemplate_stimulus, domain=DependenceOnSubstanceTemplate, range=Optional[Union[str, ChemicalClassId]])

slots.DependenceOnSubstanceTemplate_stimulus_label = Slot(uri=DEFAULT_.stimulus_label, name="DependenceOnSubstanceTemplate_stimulus_label", curie=DEFAULT_.curie('stimulus_label'),
                   model_uri=DEFAULT_.DependenceOnSubstanceTemplate_stimulus_label, domain=DependenceOnSubstanceTemplate, range=Optional[str])

slots.DependenceOnSubstanceTemplate_name = Slot(uri=RDFS.label, name="DependenceOnSubstanceTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.DependenceOnSubstanceTemplate_name, domain=DependenceOnSubstanceTemplate, range=Optional[str])

slots.DependenceOnSubstanceTemplate_definition = Slot(uri=IAO['0000115'], name="DependenceOnSubstanceTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.DependenceOnSubstanceTemplate_definition, domain=DependenceOnSubstanceTemplate, range=Optional[str])

slots.DependenceOnSubstanceTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="DependenceOnSubstanceTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.DependenceOnSubstanceTemplate_equivalentTo, domain=DependenceOnSubstanceTemplate, range=Optional[str])

slots.CongenitalTemplate_disease = Slot(uri=DEFAULT_.disease, name="CongenitalTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.CongenitalTemplate_disease, domain=CongenitalTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.CongenitalTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="CongenitalTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.CongenitalTemplate_disease_label, domain=CongenitalTemplate, range=Optional[str])

slots.CongenitalTemplate_name = Slot(uri=RDFS.label, name="CongenitalTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.CongenitalTemplate_name, domain=CongenitalTemplate, range=Optional[str])

slots.CongenitalTemplate_definition = Slot(uri=IAO['0000115'], name="CongenitalTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.CongenitalTemplate_definition, domain=CongenitalTemplate, range=Optional[str])

slots.CongenitalTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="CongenitalTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.CongenitalTemplate_equivalentTo, domain=CongenitalTemplate, range=Optional[str])

slots.ChildhoodTemplate_disease = Slot(uri=DEFAULT_.disease, name="ChildhoodTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.ChildhoodTemplate_disease, domain=ChildhoodTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.ChildhoodTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="ChildhoodTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.ChildhoodTemplate_disease_label, domain=ChildhoodTemplate, range=Optional[str])

slots.ChildhoodTemplate_name = Slot(uri=RDFS.label, name="ChildhoodTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.ChildhoodTemplate_name, domain=ChildhoodTemplate, range=Optional[str])

slots.ChildhoodTemplate_definition = Slot(uri=IAO['0000115'], name="ChildhoodTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.ChildhoodTemplate_definition, domain=ChildhoodTemplate, range=Optional[str])

slots.ChildhoodTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="ChildhoodTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.ChildhoodTemplate_equivalentTo, domain=ChildhoodTemplate, range=Optional[str])

slots.AdultTemplate_disease = Slot(uri=DEFAULT_.disease, name="AdultTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.AdultTemplate_disease, domain=AdultTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.AdultTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="AdultTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.AdultTemplate_disease_label, domain=AdultTemplate, range=Optional[str])

slots.AdultTemplate_name = Slot(uri=RDFS.label, name="AdultTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AdultTemplate_name, domain=AdultTemplate, range=Optional[str])

slots.AdultTemplate_definition = Slot(uri=IAO['0000115'], name="AdultTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AdultTemplate_definition, domain=AdultTemplate, range=Optional[str])

slots.AdultTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AdultTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AdultTemplate_equivalentTo, domain=AdultTemplate, range=Optional[str])

slots.AnatomicalEntityOrCellClass_subclass_of = Slot(uri=RDFS.subclass_of, name="AnatomicalEntityOrCellClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.AnatomicalEntityOrCellClass_subclass_of, domain=AnatomicalEntityOrCellClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.LocationTemplate_disease = Slot(uri=DEFAULT_.disease, name="LocationTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.LocationTemplate_disease, domain=LocationTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.LocationTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="LocationTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.LocationTemplate_disease_label, domain=LocationTemplate, range=Optional[str])

slots.LocationTemplate_location = Slot(uri=DEFAULT_.location, name="LocationTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.LocationTemplate_location, domain=LocationTemplate, range=Optional[Union[str, AnatomicalEntityOrCellClassId]])

slots.LocationTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="LocationTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.LocationTemplate_location_label, domain=LocationTemplate, range=Optional[str])

slots.LocationTemplate_name = Slot(uri=RDFS.label, name="LocationTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.LocationTemplate_name, domain=LocationTemplate, range=Optional[str])

slots.LocationTemplate_definition = Slot(uri=IAO['0000115'], name="LocationTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.LocationTemplate_definition, domain=LocationTemplate, range=Optional[str])

slots.LocationTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="LocationTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.LocationTemplate_equivalentTo, domain=LocationTemplate, range=Optional[str])

slots.DiseaseOrDisorderClass_subclass_of = Slot(uri=RDFS.subclass_of, name="DiseaseOrDisorderClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.DiseaseOrDisorderClass_subclass_of, domain=DiseaseOrDisorderClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.InheritedSusceptibilityTemplate_disease = Slot(uri=DEFAULT_.disease, name="InheritedSusceptibilityTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.InheritedSusceptibilityTemplate_disease, domain=InheritedSusceptibilityTemplate, range=Optional[Union[str, DiseaseOrDisorderClassId]])

slots.InheritedSusceptibilityTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="InheritedSusceptibilityTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.InheritedSusceptibilityTemplate_disease_label, domain=InheritedSusceptibilityTemplate, range=Optional[str])

slots.InheritedSusceptibilityTemplate_name = Slot(uri=RDFS.label, name="InheritedSusceptibilityTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.InheritedSusceptibilityTemplate_name, domain=InheritedSusceptibilityTemplate, range=Optional[str])

slots.InheritedSusceptibilityTemplate_definition = Slot(uri=IAO['0000115'], name="InheritedSusceptibilityTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.InheritedSusceptibilityTemplate_definition, domain=InheritedSusceptibilityTemplate, range=Optional[str])

slots.InheritedSusceptibilityTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="InheritedSusceptibilityTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.InheritedSusceptibilityTemplate_equivalentTo, domain=InheritedSusceptibilityTemplate, range=Optional[str])

slots.AdenocarcinomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="AdenocarcinomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.AdenocarcinomaDiseaseHasLocationXTemplate_location, domain=AdenocarcinomaDiseaseHasLocationXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.AdenocarcinomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="AdenocarcinomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.AdenocarcinomaDiseaseHasLocationXTemplate_location_label, domain=AdenocarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.AdenocarcinomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="AdenocarcinomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AdenocarcinomaDiseaseHasLocationXTemplate_name, domain=AdenocarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.AdenocarcinomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="AdenocarcinomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AdenocarcinomaDiseaseHasLocationXTemplate_definition, domain=AdenocarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.AdenocarcinomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AdenocarcinomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AdenocarcinomaDiseaseHasLocationXTemplate_equivalentTo, domain=AdenocarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LipomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="LipomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.LipomaDiseaseHasLocationXTemplate_location, domain=LipomaDiseaseHasLocationXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.LipomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="LipomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.LipomaDiseaseHasLocationXTemplate_location_label, domain=LipomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LipomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="LipomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.LipomaDiseaseHasLocationXTemplate_name, domain=LipomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LipomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="LipomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.LipomaDiseaseHasLocationXTemplate_definition, domain=LipomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LipomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="LipomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.LipomaDiseaseHasLocationXTemplate_equivalentTo, domain=LipomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.AnatomicalEntityClass_subclass_of = Slot(uri=RDFS.subclass_of, name="AnatomicalEntityClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.AnatomicalEntityClass_subclass_of, domain=AnatomicalEntityClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.MeningiomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="MeningiomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.MeningiomaDiseaseHasLocationXTemplate_location, domain=MeningiomaDiseaseHasLocationXTemplate, range=Optional[Union[str, AnatomicalEntityClassId]])

slots.MeningiomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="MeningiomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.MeningiomaDiseaseHasLocationXTemplate_location_label, domain=MeningiomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.MeningiomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="MeningiomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.MeningiomaDiseaseHasLocationXTemplate_name, domain=MeningiomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.MeningiomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="MeningiomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.MeningiomaDiseaseHasLocationXTemplate_definition, domain=MeningiomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.MeningiomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="MeningiomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.MeningiomaDiseaseHasLocationXTemplate_equivalentTo, domain=MeningiomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_process = Slot(uri=DEFAULT_.process, name="DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_process", curie=DEFAULT_.curie('process'),
                   model_uri=DEFAULT_.DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_process, domain=DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_process_label = Slot(uri=DEFAULT_.process_label, name="DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_process_label", curie=DEFAULT_.curie('process_label'),
                   model_uri=DEFAULT_.DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_process_label, domain=DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate, range=Optional[str])

slots.DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_name = Slot(uri=RDFS.label, name="DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_name, domain=DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate, range=Optional[str])

slots.DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_definition = Slot(uri=IAO['0000115'], name="DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_definition, domain=DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate, range=Optional[str])

slots.DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate_equivalentTo, domain=DiseaseOrDisorderDiseaseCausedByDisruptionOfXTemplate, range=Optional[str])

slots.InfectiousDiseaseClass_subclass_of = Slot(uri=RDFS.subclass_of, name="InfectiousDiseaseClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.InfectiousDiseaseClass_subclass_of, domain=InfectiousDiseaseClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.PostinfectiousDiseaseTemplate_disease = Slot(uri=DEFAULT_.disease, name="PostinfectiousDiseaseTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.PostinfectiousDiseaseTemplate_disease, domain=PostinfectiousDiseaseTemplate, range=Optional[Union[str, OrganismClassId]])

slots.PostinfectiousDiseaseTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="PostinfectiousDiseaseTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.PostinfectiousDiseaseTemplate_disease_label, domain=PostinfectiousDiseaseTemplate, range=Optional[str])

slots.PostinfectiousDiseaseTemplate_feature = Slot(uri=DEFAULT_.feature, name="PostinfectiousDiseaseTemplate_feature", curie=DEFAULT_.curie('feature'),
                   model_uri=DEFAULT_.PostinfectiousDiseaseTemplate_feature, domain=PostinfectiousDiseaseTemplate, range=Optional[Union[str, InfectiousDiseaseClassId]])

slots.PostinfectiousDiseaseTemplate_feature_label = Slot(uri=DEFAULT_.feature_label, name="PostinfectiousDiseaseTemplate_feature_label", curie=DEFAULT_.curie('feature_label'),
                   model_uri=DEFAULT_.PostinfectiousDiseaseTemplate_feature_label, domain=PostinfectiousDiseaseTemplate, range=Optional[str])

slots.PostinfectiousDiseaseTemplate_name = Slot(uri=RDFS.label, name="PostinfectiousDiseaseTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.PostinfectiousDiseaseTemplate_name, domain=PostinfectiousDiseaseTemplate, range=Optional[str])

slots.PostinfectiousDiseaseTemplate_definition = Slot(uri=IAO['0000115'], name="PostinfectiousDiseaseTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.PostinfectiousDiseaseTemplate_definition, domain=PostinfectiousDiseaseTemplate, range=Optional[str])

slots.PostinfectiousDiseaseTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="PostinfectiousDiseaseTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.PostinfectiousDiseaseTemplate_equivalentTo, domain=PostinfectiousDiseaseTemplate, range=Optional[str])

slots.ProcessClass_subclass_of = Slot(uri=RDFS.subclass_of, name="ProcessClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.ProcessClass_subclass_of, domain=ProcessClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.BasisInDisruptionOfProcessTemplate_process = Slot(uri=DEFAULT_.process, name="BasisInDisruptionOfProcessTemplate_process", curie=DEFAULT_.curie('process'),
                   model_uri=DEFAULT_.BasisInDisruptionOfProcessTemplate_process, domain=BasisInDisruptionOfProcessTemplate, range=Optional[Union[str, ProcessClassId]])

slots.BasisInDisruptionOfProcessTemplate_process_label = Slot(uri=DEFAULT_.process_label, name="BasisInDisruptionOfProcessTemplate_process_label", curie=DEFAULT_.curie('process_label'),
                   model_uri=DEFAULT_.BasisInDisruptionOfProcessTemplate_process_label, domain=BasisInDisruptionOfProcessTemplate, range=Optional[str])

slots.BasisInDisruptionOfProcessTemplate_name = Slot(uri=RDFS.label, name="BasisInDisruptionOfProcessTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.BasisInDisruptionOfProcessTemplate_name, domain=BasisInDisruptionOfProcessTemplate, range=Optional[str])

slots.BasisInDisruptionOfProcessTemplate_definition = Slot(uri=IAO['0000115'], name="BasisInDisruptionOfProcessTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.BasisInDisruptionOfProcessTemplate_definition, domain=BasisInDisruptionOfProcessTemplate, range=Optional[str])

slots.BasisInDisruptionOfProcessTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="BasisInDisruptionOfProcessTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.BasisInDisruptionOfProcessTemplate_equivalentTo, domain=BasisInDisruptionOfProcessTemplate, range=Optional[str])

slots.DiseaseSeriesByGeneTemplate_disease = Slot(uri=DEFAULT_.disease, name="DiseaseSeriesByGeneTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneTemplate_disease, domain=DiseaseSeriesByGeneTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.DiseaseSeriesByGeneTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="DiseaseSeriesByGeneTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneTemplate_disease_label, domain=DiseaseSeriesByGeneTemplate, range=Optional[str])

slots.DiseaseSeriesByGeneTemplate_gene = Slot(uri=DEFAULT_.gene, name="DiseaseSeriesByGeneTemplate_gene", curie=DEFAULT_.curie('gene'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneTemplate_gene, domain=DiseaseSeriesByGeneTemplate, range=Optional[Union[str, GeneClassId]])

slots.DiseaseSeriesByGeneTemplate_gene_label = Slot(uri=DEFAULT_.gene_label, name="DiseaseSeriesByGeneTemplate_gene_label", curie=DEFAULT_.curie('gene_label'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneTemplate_gene_label, domain=DiseaseSeriesByGeneTemplate, range=Optional[str])

slots.DiseaseSeriesByGeneTemplate_name = Slot(uri=RDFS.label, name="DiseaseSeriesByGeneTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneTemplate_name, domain=DiseaseSeriesByGeneTemplate, range=Optional[str])

slots.DiseaseSeriesByGeneTemplate_definition = Slot(uri=IAO['0000115'], name="DiseaseSeriesByGeneTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneTemplate_definition, domain=DiseaseSeriesByGeneTemplate, range=Optional[str])

slots.DiseaseSeriesByGeneTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="DiseaseSeriesByGeneTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.DiseaseSeriesByGeneTemplate_equivalentTo, domain=DiseaseSeriesByGeneTemplate, range=Optional[str])

slots.LeiomyomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="LeiomyomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.LeiomyomaDiseaseHasLocationXTemplate_location, domain=LeiomyomaDiseaseHasLocationXTemplate, range=Optional[Union[str, AnatomicalEntityClassId]])

slots.LeiomyomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="LeiomyomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.LeiomyomaDiseaseHasLocationXTemplate_location_label, domain=LeiomyomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LeiomyomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="LeiomyomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.LeiomyomaDiseaseHasLocationXTemplate_name, domain=LeiomyomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LeiomyomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="LeiomyomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.LeiomyomaDiseaseHasLocationXTemplate_definition, domain=LeiomyomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LeiomyomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="LeiomyomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.LeiomyomaDiseaseHasLocationXTemplate_equivalentTo, domain=LeiomyomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.RhabdomyosarcomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="RhabdomyosarcomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.RhabdomyosarcomaDiseaseHasLocationXTemplate_location, domain=RhabdomyosarcomaDiseaseHasLocationXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.RhabdomyosarcomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="RhabdomyosarcomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.RhabdomyosarcomaDiseaseHasLocationXTemplate_location_label, domain=RhabdomyosarcomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.RhabdomyosarcomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="RhabdomyosarcomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.RhabdomyosarcomaDiseaseHasLocationXTemplate_name, domain=RhabdomyosarcomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.RhabdomyosarcomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="RhabdomyosarcomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.RhabdomyosarcomaDiseaseHasLocationXTemplate_definition, domain=RhabdomyosarcomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.RhabdomyosarcomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="RhabdomyosarcomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.RhabdomyosarcomaDiseaseHasLocationXTemplate_equivalentTo, domain=RhabdomyosarcomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.VectorBorneDiseaseTemplate_infectious_disease = Slot(uri=DEFAULT_.infectious_disease, name="VectorBorneDiseaseTemplate_infectious_disease", curie=DEFAULT_.curie('infectious_disease'),
                   model_uri=DEFAULT_.VectorBorneDiseaseTemplate_infectious_disease, domain=VectorBorneDiseaseTemplate, range=Optional[Union[str, InfectiousDiseaseClassId]])

slots.VectorBorneDiseaseTemplate_infectious_disease_label = Slot(uri=DEFAULT_.infectious_disease_label, name="VectorBorneDiseaseTemplate_infectious_disease_label", curie=DEFAULT_.curie('infectious_disease_label'),
                   model_uri=DEFAULT_.VectorBorneDiseaseTemplate_infectious_disease_label, domain=VectorBorneDiseaseTemplate, range=Optional[str])

slots.VectorBorneDiseaseTemplate_vector = Slot(uri=DEFAULT_.vector, name="VectorBorneDiseaseTemplate_vector", curie=DEFAULT_.curie('vector'),
                   model_uri=DEFAULT_.VectorBorneDiseaseTemplate_vector, domain=VectorBorneDiseaseTemplate, range=Optional[Union[str, OrganismClassId]])

slots.VectorBorneDiseaseTemplate_vector_label = Slot(uri=DEFAULT_.vector_label, name="VectorBorneDiseaseTemplate_vector_label", curie=DEFAULT_.curie('vector_label'),
                   model_uri=DEFAULT_.VectorBorneDiseaseTemplate_vector_label, domain=VectorBorneDiseaseTemplate, range=Optional[str])

slots.VectorBorneDiseaseTemplate_name = Slot(uri=RDFS.label, name="VectorBorneDiseaseTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.VectorBorneDiseaseTemplate_name, domain=VectorBorneDiseaseTemplate, range=Optional[str])

slots.VectorBorneDiseaseTemplate_definition = Slot(uri=IAO['0000115'], name="VectorBorneDiseaseTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.VectorBorneDiseaseTemplate_definition, domain=VectorBorneDiseaseTemplate, range=Optional[str])

slots.VectorBorneDiseaseTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="VectorBorneDiseaseTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.VectorBorneDiseaseTemplate_equivalentTo, domain=VectorBorneDiseaseTemplate, range=Optional[str])

slots.InflammatoryDiseaseBySiteTemplate_location = Slot(uri=DEFAULT_.location, name="InflammatoryDiseaseBySiteTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.InflammatoryDiseaseBySiteTemplate_location, domain=InflammatoryDiseaseBySiteTemplate, range=Optional[Union[str, AnatomicalStructureClassId]])

slots.InflammatoryDiseaseBySiteTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="InflammatoryDiseaseBySiteTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.InflammatoryDiseaseBySiteTemplate_location_label, domain=InflammatoryDiseaseBySiteTemplate, range=Optional[str])

slots.InflammatoryDiseaseBySiteTemplate_name = Slot(uri=RDFS.label, name="InflammatoryDiseaseBySiteTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.InflammatoryDiseaseBySiteTemplate_name, domain=InflammatoryDiseaseBySiteTemplate, range=Optional[str])

slots.InflammatoryDiseaseBySiteTemplate_definition = Slot(uri=IAO['0000115'], name="InflammatoryDiseaseBySiteTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.InflammatoryDiseaseBySiteTemplate_definition, domain=InflammatoryDiseaseBySiteTemplate, range=Optional[str])

slots.InflammatoryDiseaseBySiteTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="InflammatoryDiseaseBySiteTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.InflammatoryDiseaseBySiteTemplate_equivalentTo, domain=InflammatoryDiseaseBySiteTemplate, range=Optional[str])

slots.YLinkedTemplate_disease = Slot(uri=DEFAULT_.disease, name="YLinkedTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.YLinkedTemplate_disease, domain=YLinkedTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.YLinkedTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="YLinkedTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.YLinkedTemplate_disease_label, domain=YLinkedTemplate, range=Optional[str])

slots.YLinkedTemplate_name = Slot(uri=RDFS.label, name="YLinkedTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.YLinkedTemplate_name, domain=YLinkedTemplate, range=Optional[str])

slots.YLinkedTemplate_definition = Slot(uri=IAO['0000115'], name="YLinkedTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.YLinkedTemplate_definition, domain=YLinkedTemplate, range=Optional[str])

slots.YLinkedTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="YLinkedTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.YLinkedTemplate_equivalentTo, domain=YLinkedTemplate, range=Optional[str])

slots.NeoendocrineNeoplasmTemplate_location = Slot(uri=DEFAULT_.location, name="NeoendocrineNeoplasmTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.NeoendocrineNeoplasmTemplate_location, domain=NeoendocrineNeoplasmTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.NeoendocrineNeoplasmTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="NeoendocrineNeoplasmTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.NeoendocrineNeoplasmTemplate_location_label, domain=NeoendocrineNeoplasmTemplate, range=Optional[str])

slots.NeoendocrineNeoplasmTemplate_name = Slot(uri=RDFS.label, name="NeoendocrineNeoplasmTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.NeoendocrineNeoplasmTemplate_name, domain=NeoendocrineNeoplasmTemplate, range=Optional[str])

slots.NeoendocrineNeoplasmTemplate_definition = Slot(uri=IAO['0000115'], name="NeoendocrineNeoplasmTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.NeoendocrineNeoplasmTemplate_definition, domain=NeoendocrineNeoplasmTemplate, range=Optional[str])

slots.NeoendocrineNeoplasmTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="NeoendocrineNeoplasmTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.NeoendocrineNeoplasmTemplate_equivalentTo, domain=NeoendocrineNeoplasmTemplate, range=Optional[str])

slots.OMIMPhenotypicSeriesTemplate_disease = Slot(uri=DEFAULT_.disease, name="OMIMPhenotypicSeriesTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.OMIMPhenotypicSeriesTemplate_disease, domain=OMIMPhenotypicSeriesTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.OMIMPhenotypicSeriesTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="OMIMPhenotypicSeriesTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.OMIMPhenotypicSeriesTemplate_disease_label, domain=OMIMPhenotypicSeriesTemplate, range=Optional[str])

slots.OMIMPhenotypicSeriesTemplate_name = Slot(uri=RDFS.label, name="OMIMPhenotypicSeriesTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.OMIMPhenotypicSeriesTemplate_name, domain=OMIMPhenotypicSeriesTemplate, range=Optional[str])

slots.LeiomyosarcomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="LeiomyosarcomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.LeiomyosarcomaDiseaseHasLocationXTemplate_location, domain=LeiomyosarcomaDiseaseHasLocationXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.LeiomyosarcomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="LeiomyosarcomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.LeiomyosarcomaDiseaseHasLocationXTemplate_location_label, domain=LeiomyosarcomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LeiomyosarcomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="LeiomyosarcomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.LeiomyosarcomaDiseaseHasLocationXTemplate_name, domain=LeiomyosarcomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LeiomyosarcomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="LeiomyosarcomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.LeiomyosarcomaDiseaseHasLocationXTemplate_definition, domain=LeiomyosarcomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LeiomyosarcomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="LeiomyosarcomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.LeiomyosarcomaDiseaseHasLocationXTemplate_equivalentTo, domain=LeiomyosarcomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.CancerTemplate_location = Slot(uri=DEFAULT_.location, name="CancerTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.CancerTemplate_location, domain=CancerTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.CancerTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="CancerTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.CancerTemplate_location_label, domain=CancerTemplate, range=Optional[str])

slots.CancerTemplate_name = Slot(uri=RDFS.label, name="CancerTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.CancerTemplate_name, domain=CancerTemplate, range=Optional[str])

slots.CancerTemplate_definition = Slot(uri=IAO['0000115'], name="CancerTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.CancerTemplate_definition, domain=CancerTemplate, range=Optional[str])

slots.CancerTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="CancerTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.CancerTemplate_equivalentTo, domain=CancerTemplate, range=Optional[str])

slots.NeoendocrineNeoplasmGrade1Template_location = Slot(uri=DEFAULT_.location, name="NeoendocrineNeoplasmGrade1Template_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.NeoendocrineNeoplasmGrade1Template_location, domain=NeoendocrineNeoplasmGrade1Template, range=Optional[Union[str, OwlThingClassId]])

slots.NeoendocrineNeoplasmGrade1Template_location_label = Slot(uri=DEFAULT_.location_label, name="NeoendocrineNeoplasmGrade1Template_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.NeoendocrineNeoplasmGrade1Template_location_label, domain=NeoendocrineNeoplasmGrade1Template, range=Optional[str])

slots.NeoendocrineNeoplasmGrade1Template_name = Slot(uri=RDFS.label, name="NeoendocrineNeoplasmGrade1Template_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.NeoendocrineNeoplasmGrade1Template_name, domain=NeoendocrineNeoplasmGrade1Template, range=Optional[str])

slots.NeoendocrineNeoplasmGrade1Template_definition = Slot(uri=IAO['0000115'], name="NeoendocrineNeoplasmGrade1Template_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.NeoendocrineNeoplasmGrade1Template_definition, domain=NeoendocrineNeoplasmGrade1Template, range=Optional[str])

slots.NeoendocrineNeoplasmGrade1Template_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="NeoendocrineNeoplasmGrade1Template_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.NeoendocrineNeoplasmGrade1Template_equivalentTo, domain=NeoendocrineNeoplasmGrade1Template, range=Optional[str])

slots.InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_process = Slot(uri=DEFAULT_.process, name="InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_process", curie=DEFAULT_.curie('process'),
                   model_uri=DEFAULT_.InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_process, domain=InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_process_label = Slot(uri=DEFAULT_.process_label, name="InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_process_label", curie=DEFAULT_.curie('process_label'),
                   model_uri=DEFAULT_.InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_process_label, domain=InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate, range=Optional[str])

slots.InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_name = Slot(uri=RDFS.label, name="InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_name, domain=InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate, range=Optional[str])

slots.InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_definition = Slot(uri=IAO['0000115'], name="InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_definition, domain=InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate, range=Optional[str])

slots.InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate_equivalentTo, domain=InbornErrorsOfMetabolismDiseaseCausedByDisruptionOfXTemplate, range=Optional[str])

slots.BenignNeoplasmTemplate_location = Slot(uri=DEFAULT_.location, name="BenignNeoplasmTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.BenignNeoplasmTemplate_location, domain=BenignNeoplasmTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.BenignNeoplasmTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="BenignNeoplasmTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.BenignNeoplasmTemplate_location_label, domain=BenignNeoplasmTemplate, range=Optional[str])

slots.BenignNeoplasmTemplate_name = Slot(uri=RDFS.label, name="BenignNeoplasmTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.BenignNeoplasmTemplate_name, domain=BenignNeoplasmTemplate, range=Optional[str])

slots.BenignNeoplasmTemplate_definition = Slot(uri=IAO['0000115'], name="BenignNeoplasmTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.BenignNeoplasmTemplate_definition, domain=BenignNeoplasmTemplate, range=Optional[str])

slots.BenignNeoplasmTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="BenignNeoplasmTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.BenignNeoplasmTemplate_equivalentTo, domain=BenignNeoplasmTemplate, range=Optional[str])

slots.CarcinomaTemplate_location = Slot(uri=DEFAULT_.location, name="CarcinomaTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.CarcinomaTemplate_location, domain=CarcinomaTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.CarcinomaTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="CarcinomaTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.CarcinomaTemplate_location_label, domain=CarcinomaTemplate, range=Optional[str])

slots.CarcinomaTemplate_name = Slot(uri=RDFS.label, name="CarcinomaTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.CarcinomaTemplate_name, domain=CarcinomaTemplate, range=Optional[str])

slots.CarcinomaTemplate_definition = Slot(uri=IAO['0000115'], name="CarcinomaTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.CarcinomaTemplate_definition, domain=CarcinomaTemplate, range=Optional[str])

slots.CarcinomaTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="CarcinomaTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.CarcinomaTemplate_equivalentTo, domain=CarcinomaTemplate, range=Optional[str])

slots.InfectiousDiseaseByAgentTemplate_agent = Slot(uri=DEFAULT_.agent, name="InfectiousDiseaseByAgentTemplate_agent", curie=DEFAULT_.curie('agent'),
                   model_uri=DEFAULT_.InfectiousDiseaseByAgentTemplate_agent, domain=InfectiousDiseaseByAgentTemplate, range=Optional[Union[str, OrganismClassId]])

slots.InfectiousDiseaseByAgentTemplate_agent_label = Slot(uri=DEFAULT_.agent_label, name="InfectiousDiseaseByAgentTemplate_agent_label", curie=DEFAULT_.curie('agent_label'),
                   model_uri=DEFAULT_.InfectiousDiseaseByAgentTemplate_agent_label, domain=InfectiousDiseaseByAgentTemplate, range=Optional[str])

slots.InfectiousDiseaseByAgentTemplate_name = Slot(uri=RDFS.label, name="InfectiousDiseaseByAgentTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.InfectiousDiseaseByAgentTemplate_name, domain=InfectiousDiseaseByAgentTemplate, range=Optional[str])

slots.InfectiousDiseaseByAgentTemplate_definition = Slot(uri=IAO['0000115'], name="InfectiousDiseaseByAgentTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.InfectiousDiseaseByAgentTemplate_definition, domain=InfectiousDiseaseByAgentTemplate, range=Optional[str])

slots.InfectiousDiseaseByAgentTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="InfectiousDiseaseByAgentTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.InfectiousDiseaseByAgentTemplate_equivalentTo, domain=InfectiousDiseaseByAgentTemplate, range=Optional[str])

slots.RareGeneticTemplate_disease = Slot(uri=DEFAULT_.disease, name="RareGeneticTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.RareGeneticTemplate_disease, domain=RareGeneticTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.RareGeneticTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="RareGeneticTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.RareGeneticTemplate_disease_label, domain=RareGeneticTemplate, range=Optional[str])

slots.RareGeneticTemplate_name = Slot(uri=RDFS.label, name="RareGeneticTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.RareGeneticTemplate_name, domain=RareGeneticTemplate, range=Optional[str])

slots.RareGeneticTemplate_definition = Slot(uri=IAO['0000115'], name="RareGeneticTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.RareGeneticTemplate_definition, domain=RareGeneticTemplate, range=Optional[str])

slots.RareGeneticTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="RareGeneticTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.RareGeneticTemplate_equivalentTo, domain=RareGeneticTemplate, range=Optional[str])

slots.XDiseaseHasBasisInDysfunctionOfXTemplate_disease = Slot(uri=DEFAULT_.disease, name="XDiseaseHasBasisInDysfunctionOfXTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.XDiseaseHasBasisInDysfunctionOfXTemplate_disease, domain=XDiseaseHasBasisInDysfunctionOfXTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.XDiseaseHasBasisInDysfunctionOfXTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="XDiseaseHasBasisInDysfunctionOfXTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.XDiseaseHasBasisInDysfunctionOfXTemplate_disease_label, domain=XDiseaseHasBasisInDysfunctionOfXTemplate, range=Optional[str])

slots.XDiseaseHasBasisInDysfunctionOfXTemplate_structure = Slot(uri=DEFAULT_.structure, name="XDiseaseHasBasisInDysfunctionOfXTemplate_structure", curie=DEFAULT_.curie('structure'),
                   model_uri=DEFAULT_.XDiseaseHasBasisInDysfunctionOfXTemplate_structure, domain=XDiseaseHasBasisInDysfunctionOfXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.XDiseaseHasBasisInDysfunctionOfXTemplate_structure_label = Slot(uri=DEFAULT_.structure_label, name="XDiseaseHasBasisInDysfunctionOfXTemplate_structure_label", curie=DEFAULT_.curie('structure_label'),
                   model_uri=DEFAULT_.XDiseaseHasBasisInDysfunctionOfXTemplate_structure_label, domain=XDiseaseHasBasisInDysfunctionOfXTemplate, range=Optional[str])

slots.XDiseaseHasBasisInDysfunctionOfXTemplate_name = Slot(uri=RDFS.label, name="XDiseaseHasBasisInDysfunctionOfXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.XDiseaseHasBasisInDysfunctionOfXTemplate_name, domain=XDiseaseHasBasisInDysfunctionOfXTemplate, range=Optional[str])

slots.XDiseaseHasBasisInDysfunctionOfXTemplate_definition = Slot(uri=IAO['0000115'], name="XDiseaseHasBasisInDysfunctionOfXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.XDiseaseHasBasisInDysfunctionOfXTemplate_definition, domain=XDiseaseHasBasisInDysfunctionOfXTemplate, range=Optional[str])

slots.XDiseaseHasBasisInDysfunctionOfXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="XDiseaseHasBasisInDysfunctionOfXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.XDiseaseHasBasisInDysfunctionOfXTemplate_equivalentTo, domain=XDiseaseHasBasisInDysfunctionOfXTemplate, range=Optional[str])

slots.SubstanceAbuseTemplate_stimulus = Slot(uri=DEFAULT_.stimulus, name="SubstanceAbuseTemplate_stimulus", curie=DEFAULT_.curie('stimulus'),
                   model_uri=DEFAULT_.SubstanceAbuseTemplate_stimulus, domain=SubstanceAbuseTemplate, range=Optional[Union[str, MaterialEntityClassId]])

slots.SubstanceAbuseTemplate_stimulus_label = Slot(uri=DEFAULT_.stimulus_label, name="SubstanceAbuseTemplate_stimulus_label", curie=DEFAULT_.curie('stimulus_label'),
                   model_uri=DEFAULT_.SubstanceAbuseTemplate_stimulus_label, domain=SubstanceAbuseTemplate, range=Optional[str])

slots.SubstanceAbuseTemplate_name = Slot(uri=RDFS.label, name="SubstanceAbuseTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.SubstanceAbuseTemplate_name, domain=SubstanceAbuseTemplate, range=Optional[str])

slots.SubstanceAbuseTemplate_definition = Slot(uri=IAO['0000115'], name="SubstanceAbuseTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.SubstanceAbuseTemplate_definition, domain=SubstanceAbuseTemplate, range=Optional[str])

slots.SubstanceAbuseTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="SubstanceAbuseTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.SubstanceAbuseTemplate_equivalentTo, domain=SubstanceAbuseTemplate, range=Optional[str])

slots.HemangiomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="HemangiomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.HemangiomaDiseaseHasLocationXTemplate_location, domain=HemangiomaDiseaseHasLocationXTemplate, range=Optional[Union[str, AnatomicalEntityClassId]])

slots.HemangiomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="HemangiomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.HemangiomaDiseaseHasLocationXTemplate_location_label, domain=HemangiomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.HemangiomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="HemangiomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.HemangiomaDiseaseHasLocationXTemplate_name, domain=HemangiomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.HemangiomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="HemangiomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.HemangiomaDiseaseHasLocationXTemplate_definition, domain=HemangiomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.HemangiomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="HemangiomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.HemangiomaDiseaseHasLocationXTemplate_equivalentTo, domain=HemangiomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.ConsequenceOfInfectiousDiseaseTemplate_parent = Slot(uri=DEFAULT_.parent, name="ConsequenceOfInfectiousDiseaseTemplate_parent", curie=DEFAULT_.curie('parent'),
                   model_uri=DEFAULT_.ConsequenceOfInfectiousDiseaseTemplate_parent, domain=ConsequenceOfInfectiousDiseaseTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.ConsequenceOfInfectiousDiseaseTemplate_parent_label = Slot(uri=DEFAULT_.parent_label, name="ConsequenceOfInfectiousDiseaseTemplate_parent_label", curie=DEFAULT_.curie('parent_label'),
                   model_uri=DEFAULT_.ConsequenceOfInfectiousDiseaseTemplate_parent_label, domain=ConsequenceOfInfectiousDiseaseTemplate, range=Optional[str])

slots.ConsequenceOfInfectiousDiseaseTemplate_cause = Slot(uri=DEFAULT_.cause, name="ConsequenceOfInfectiousDiseaseTemplate_cause", curie=DEFAULT_.curie('cause'),
                   model_uri=DEFAULT_.ConsequenceOfInfectiousDiseaseTemplate_cause, domain=ConsequenceOfInfectiousDiseaseTemplate, range=Optional[Union[str, InfectiousDiseaseClassId]])

slots.ConsequenceOfInfectiousDiseaseTemplate_cause_label = Slot(uri=DEFAULT_.cause_label, name="ConsequenceOfInfectiousDiseaseTemplate_cause_label", curie=DEFAULT_.curie('cause_label'),
                   model_uri=DEFAULT_.ConsequenceOfInfectiousDiseaseTemplate_cause_label, domain=ConsequenceOfInfectiousDiseaseTemplate, range=Optional[str])

slots.ConsequenceOfInfectiousDiseaseTemplate_name = Slot(uri=RDFS.label, name="ConsequenceOfInfectiousDiseaseTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.ConsequenceOfInfectiousDiseaseTemplate_name, domain=ConsequenceOfInfectiousDiseaseTemplate, range=Optional[str])

slots.ConsequenceOfInfectiousDiseaseTemplate_definition = Slot(uri=IAO['0000115'], name="ConsequenceOfInfectiousDiseaseTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.ConsequenceOfInfectiousDiseaseTemplate_definition, domain=ConsequenceOfInfectiousDiseaseTemplate, range=Optional[str])

slots.ConsequenceOfInfectiousDiseaseTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="ConsequenceOfInfectiousDiseaseTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.ConsequenceOfInfectiousDiseaseTemplate_equivalentTo, domain=ConsequenceOfInfectiousDiseaseTemplate, range=Optional[str])

slots.InbornMetabolicTemplate_process = Slot(uri=DEFAULT_.process, name="InbornMetabolicTemplate_process", curie=DEFAULT_.curie('process'),
                   model_uri=DEFAULT_.InbornMetabolicTemplate_process, domain=InbornMetabolicTemplate, range=Optional[Union[str, ProcessClassId]])

slots.InbornMetabolicTemplate_process_label = Slot(uri=DEFAULT_.process_label, name="InbornMetabolicTemplate_process_label", curie=DEFAULT_.curie('process_label'),
                   model_uri=DEFAULT_.InbornMetabolicTemplate_process_label, domain=InbornMetabolicTemplate, range=Optional[str])

slots.InbornMetabolicTemplate_name = Slot(uri=RDFS.label, name="InbornMetabolicTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.InbornMetabolicTemplate_name, domain=InbornMetabolicTemplate, range=Optional[str])

slots.InbornMetabolicTemplate_definition = Slot(uri=IAO['0000115'], name="InbornMetabolicTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.InbornMetabolicTemplate_definition, domain=InbornMetabolicTemplate, range=Optional[str])

slots.InbornMetabolicTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="InbornMetabolicTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.InbornMetabolicTemplate_equivalentTo, domain=InbornMetabolicTemplate, range=Optional[str])

slots.MalignantTemplate_neoplasm = Slot(uri=DEFAULT_.neoplasm, name="MalignantTemplate_neoplasm", curie=DEFAULT_.curie('neoplasm'),
                   model_uri=DEFAULT_.MalignantTemplate_neoplasm, domain=MalignantTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.MalignantTemplate_neoplasm_label = Slot(uri=DEFAULT_.neoplasm_label, name="MalignantTemplate_neoplasm_label", curie=DEFAULT_.curie('neoplasm_label'),
                   model_uri=DEFAULT_.MalignantTemplate_neoplasm_label, domain=MalignantTemplate, range=Optional[str])

slots.MalignantTemplate_name = Slot(uri=RDFS.label, name="MalignantTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.MalignantTemplate_name, domain=MalignantTemplate, range=Optional[str])

slots.MalignantTemplate_definition = Slot(uri=IAO['0000115'], name="MalignantTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.MalignantTemplate_definition, domain=MalignantTemplate, range=Optional[str])

slots.MalignantTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="MalignantTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.MalignantTemplate_equivalentTo, domain=MalignantTemplate, range=Optional[str])

slots.AllergyTemplate_substance = Slot(uri=DEFAULT_.substance, name="AllergyTemplate_substance", curie=DEFAULT_.curie('substance'),
                   model_uri=DEFAULT_.AllergyTemplate_substance, domain=AllergyTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.AllergyTemplate_substance_label = Slot(uri=DEFAULT_.substance_label, name="AllergyTemplate_substance_label", curie=DEFAULT_.curie('substance_label'),
                   model_uri=DEFAULT_.AllergyTemplate_substance_label, domain=AllergyTemplate, range=Optional[str])

slots.AllergyTemplate_name = Slot(uri=RDFS.label, name="AllergyTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AllergyTemplate_name, domain=AllergyTemplate, range=Optional[str])

slots.AllergyTemplate_definition = Slot(uri=IAO['0000115'], name="AllergyTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AllergyTemplate_definition, domain=AllergyTemplate, range=Optional[str])

slots.AllergyTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AllergyTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AllergyTemplate_equivalentTo, domain=AllergyTemplate, range=Optional[str])

slots.MitochondriaalSubtypeTemplate_disease = Slot(uri=DEFAULT_.disease, name="MitochondriaalSubtypeTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.MitochondriaalSubtypeTemplate_disease, domain=MitochondriaalSubtypeTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.MitochondriaalSubtypeTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="MitochondriaalSubtypeTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.MitochondriaalSubtypeTemplate_disease_label, domain=MitochondriaalSubtypeTemplate, range=Optional[str])

slots.MitochondriaalSubtypeTemplate_name = Slot(uri=RDFS.label, name="MitochondriaalSubtypeTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.MitochondriaalSubtypeTemplate_name, domain=MitochondriaalSubtypeTemplate, range=Optional[str])

slots.MitochondriaalSubtypeTemplate_definition = Slot(uri=IAO['0000115'], name="MitochondriaalSubtypeTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.MitochondriaalSubtypeTemplate_definition, domain=MitochondriaalSubtypeTemplate, range=Optional[str])

slots.MitochondriaalSubtypeTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="MitochondriaalSubtypeTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.MitochondriaalSubtypeTemplate_equivalentTo, domain=MitochondriaalSubtypeTemplate, range=Optional[str])

slots.InfectiousInflammationTemplate_location = Slot(uri=DEFAULT_.location, name="InfectiousInflammationTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.InfectiousInflammationTemplate_location, domain=InfectiousInflammationTemplate, range=Optional[Union[str, AnatomicalStructureClassId]])

slots.InfectiousInflammationTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="InfectiousInflammationTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.InfectiousInflammationTemplate_location_label, domain=InfectiousInflammationTemplate, range=Optional[str])

slots.InfectiousInflammationTemplate_agent = Slot(uri=DEFAULT_.agent, name="InfectiousInflammationTemplate_agent", curie=DEFAULT_.curie('agent'),
                   model_uri=DEFAULT_.InfectiousInflammationTemplate_agent, domain=InfectiousInflammationTemplate, range=Optional[Union[str, OrganismClassId]])

slots.InfectiousInflammationTemplate_agent_label = Slot(uri=DEFAULT_.agent_label, name="InfectiousInflammationTemplate_agent_label", curie=DEFAULT_.curie('agent_label'),
                   model_uri=DEFAULT_.InfectiousInflammationTemplate_agent_label, domain=InfectiousInflammationTemplate, range=Optional[str])

slots.InfectiousInflammationTemplate_name = Slot(uri=RDFS.label, name="InfectiousInflammationTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.InfectiousInflammationTemplate_name, domain=InfectiousInflammationTemplate, range=Optional[str])

slots.InfectiousInflammationTemplate_definition = Slot(uri=IAO['0000115'], name="InfectiousInflammationTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.InfectiousInflammationTemplate_definition, domain=InfectiousInflammationTemplate, range=Optional[str])

slots.InfectiousInflammationTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="InfectiousInflammationTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.InfectiousInflammationTemplate_equivalentTo, domain=InfectiousInflammationTemplate, range=Optional[str])

slots.NeoplasmClass_subclass_of = Slot(uri=RDFS.subclass_of, name="NeoplasmClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.NeoplasmClass_subclass_of, domain=NeoplasmClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.BenignTemplate_neoplasm = Slot(uri=DEFAULT_.neoplasm, name="BenignTemplate_neoplasm", curie=DEFAULT_.curie('neoplasm'),
                   model_uri=DEFAULT_.BenignTemplate_neoplasm, domain=BenignTemplate, range=Optional[Union[str, NeoplasmClassId]])

slots.BenignTemplate_neoplasm_label = Slot(uri=DEFAULT_.neoplasm_label, name="BenignTemplate_neoplasm_label", curie=DEFAULT_.curie('neoplasm_label'),
                   model_uri=DEFAULT_.BenignTemplate_neoplasm_label, domain=BenignTemplate, range=Optional[str])

slots.BenignTemplate_name = Slot(uri=RDFS.label, name="BenignTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.BenignTemplate_name, domain=BenignTemplate, range=Optional[str])

slots.BenignTemplate_definition = Slot(uri=IAO['0000115'], name="BenignTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.BenignTemplate_definition, domain=BenignTemplate, range=Optional[str])

slots.BenignTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="BenignTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.BenignTemplate_equivalentTo, domain=BenignTemplate, range=Optional[str])

slots.MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_location, domain=MucoepidermoidCarcinomaDiseaseHasLocationXTemplate, range=Optional[Union[str, AnatomicalEntityClassId]])

slots.MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_location_label, domain=MucoepidermoidCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_name, domain=MucoepidermoidCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_definition, domain=MucoepidermoidCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.MucoepidermoidCarcinomaDiseaseHasLocationXTemplate_equivalentTo, domain=MucoepidermoidCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.AutosomalDominantTemplate_disease = Slot(uri=DEFAULT_.disease, name="AutosomalDominantTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.AutosomalDominantTemplate_disease, domain=AutosomalDominantTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.AutosomalDominantTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="AutosomalDominantTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.AutosomalDominantTemplate_disease_label, domain=AutosomalDominantTemplate, range=Optional[str])

slots.AutosomalDominantTemplate_name = Slot(uri=RDFS.label, name="AutosomalDominantTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AutosomalDominantTemplate_name, domain=AutosomalDominantTemplate, range=Optional[str])

slots.AutosomalDominantTemplate_definition = Slot(uri=IAO['0000115'], name="AutosomalDominantTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AutosomalDominantTemplate_definition, domain=AutosomalDominantTemplate, range=Optional[str])

slots.AutosomalDominantTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AutosomalDominantTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AutosomalDominantTemplate_equivalentTo, domain=AutosomalDominantTemplate, range=Optional[str])

slots.PrimaryInfectiousTemplate_disease = Slot(uri=DEFAULT_.disease, name="PrimaryInfectiousTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.PrimaryInfectiousTemplate_disease, domain=PrimaryInfectiousTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.PrimaryInfectiousTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="PrimaryInfectiousTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.PrimaryInfectiousTemplate_disease_label, domain=PrimaryInfectiousTemplate, range=Optional[str])

slots.PrimaryInfectiousTemplate_name = Slot(uri=RDFS.label, name="PrimaryInfectiousTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.PrimaryInfectiousTemplate_name, domain=PrimaryInfectiousTemplate, range=Optional[str])

slots.PrimaryInfectiousTemplate_definition = Slot(uri=IAO['0000115'], name="PrimaryInfectiousTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.PrimaryInfectiousTemplate_definition, domain=PrimaryInfectiousTemplate, range=Optional[str])

slots.PrimaryInfectiousTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="PrimaryInfectiousTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.PrimaryInfectiousTemplate_equivalentTo, domain=PrimaryInfectiousTemplate, range=Optional[str])

slots.LymphomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="LymphomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.LymphomaDiseaseHasLocationXTemplate_location, domain=LymphomaDiseaseHasLocationXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.LymphomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="LymphomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.LymphomaDiseaseHasLocationXTemplate_location_label, domain=LymphomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LymphomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="LymphomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.LymphomaDiseaseHasLocationXTemplate_name, domain=LymphomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LymphomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="LymphomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.LymphomaDiseaseHasLocationXTemplate_definition, domain=LymphomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.LymphomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="LymphomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.LymphomaDiseaseHasLocationXTemplate_equivalentTo, domain=LymphomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.MulticellularAnatomicalStructureClass_subclass_of = Slot(uri=RDFS.subclass_of, name="MulticellularAnatomicalStructureClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.MulticellularAnatomicalStructureClass_subclass_of, domain=MulticellularAnatomicalStructureClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.AdenosquamousCarcinomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="AdenosquamousCarcinomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.AdenosquamousCarcinomaDiseaseHasLocationXTemplate_location, domain=AdenosquamousCarcinomaDiseaseHasLocationXTemplate, range=Optional[Union[str, MulticellularAnatomicalStructureClassId]])

slots.AdenosquamousCarcinomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="AdenosquamousCarcinomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.AdenosquamousCarcinomaDiseaseHasLocationXTemplate_location_label, domain=AdenosquamousCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.AdenosquamousCarcinomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="AdenosquamousCarcinomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AdenosquamousCarcinomaDiseaseHasLocationXTemplate_name, domain=AdenosquamousCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.AdenosquamousCarcinomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="AdenosquamousCarcinomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AdenosquamousCarcinomaDiseaseHasLocationXTemplate_definition, domain=AdenosquamousCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.AdenosquamousCarcinomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AdenosquamousCarcinomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AdenosquamousCarcinomaDiseaseHasLocationXTemplate_equivalentTo, domain=AdenosquamousCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.XDiseaseDisruptsXTemplate_disease = Slot(uri=DEFAULT_.disease, name="XDiseaseDisruptsXTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.XDiseaseDisruptsXTemplate_disease, domain=XDiseaseDisruptsXTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.XDiseaseDisruptsXTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="XDiseaseDisruptsXTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.XDiseaseDisruptsXTemplate_disease_label, domain=XDiseaseDisruptsXTemplate, range=Optional[str])

slots.XDiseaseDisruptsXTemplate_process = Slot(uri=DEFAULT_.process, name="XDiseaseDisruptsXTemplate_process", curie=DEFAULT_.curie('process'),
                   model_uri=DEFAULT_.XDiseaseDisruptsXTemplate_process, domain=XDiseaseDisruptsXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.XDiseaseDisruptsXTemplate_process_label = Slot(uri=DEFAULT_.process_label, name="XDiseaseDisruptsXTemplate_process_label", curie=DEFAULT_.curie('process_label'),
                   model_uri=DEFAULT_.XDiseaseDisruptsXTemplate_process_label, domain=XDiseaseDisruptsXTemplate, range=Optional[str])

slots.XDiseaseDisruptsXTemplate_name = Slot(uri=RDFS.label, name="XDiseaseDisruptsXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.XDiseaseDisruptsXTemplate_name, domain=XDiseaseDisruptsXTemplate, range=Optional[str])

slots.XDiseaseDisruptsXTemplate_definition = Slot(uri=IAO['0000115'], name="XDiseaseDisruptsXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.XDiseaseDisruptsXTemplate_definition, domain=XDiseaseDisruptsXTemplate, range=Optional[str])

slots.XDiseaseDisruptsXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="XDiseaseDisruptsXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.XDiseaseDisruptsXTemplate_equivalentTo, domain=XDiseaseDisruptsXTemplate, range=Optional[str])

slots.PoisoningTemplate_stimulus = Slot(uri=DEFAULT_.stimulus, name="PoisoningTemplate_stimulus", curie=DEFAULT_.curie('stimulus'),
                   model_uri=DEFAULT_.PoisoningTemplate_stimulus, domain=PoisoningTemplate, range=Optional[Union[str, MaterialEntityClassId]])

slots.PoisoningTemplate_stimulus_label = Slot(uri=DEFAULT_.stimulus_label, name="PoisoningTemplate_stimulus_label", curie=DEFAULT_.curie('stimulus_label'),
                   model_uri=DEFAULT_.PoisoningTemplate_stimulus_label, domain=PoisoningTemplate, range=Optional[str])

slots.PoisoningTemplate_name = Slot(uri=RDFS.label, name="PoisoningTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.PoisoningTemplate_name, domain=PoisoningTemplate, range=Optional[str])

slots.PoisoningTemplate_definition = Slot(uri=IAO['0000115'], name="PoisoningTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.PoisoningTemplate_definition, domain=PoisoningTemplate, range=Optional[str])

slots.PoisoningTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="PoisoningTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.PoisoningTemplate_equivalentTo, domain=PoisoningTemplate, range=Optional[str])

slots.SusceptibilityByGeneTemplate_gene = Slot(uri=DEFAULT_.gene, name="SusceptibilityByGeneTemplate_gene", curie=DEFAULT_.curie('gene'),
                   model_uri=DEFAULT_.SusceptibilityByGeneTemplate_gene, domain=SusceptibilityByGeneTemplate, range=Optional[Union[str, GeneClassId]])

slots.SusceptibilityByGeneTemplate_gene_label = Slot(uri=DEFAULT_.gene_label, name="SusceptibilityByGeneTemplate_gene_label", curie=DEFAULT_.curie('gene_label'),
                   model_uri=DEFAULT_.SusceptibilityByGeneTemplate_gene_label, domain=SusceptibilityByGeneTemplate, range=Optional[str])

slots.SusceptibilityByGeneTemplate_disease = Slot(uri=DEFAULT_.disease, name="SusceptibilityByGeneTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.SusceptibilityByGeneTemplate_disease, domain=SusceptibilityByGeneTemplate, range=Optional[Union[str, DiseaseOrDisorderClassId]])

slots.SusceptibilityByGeneTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="SusceptibilityByGeneTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.SusceptibilityByGeneTemplate_disease_label, domain=SusceptibilityByGeneTemplate, range=Optional[str])

slots.SusceptibilityByGeneTemplate_name = Slot(uri=RDFS.label, name="SusceptibilityByGeneTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.SusceptibilityByGeneTemplate_name, domain=SusceptibilityByGeneTemplate, range=Optional[str])

slots.SusceptibilityByGeneTemplate_definition = Slot(uri=IAO['0000115'], name="SusceptibilityByGeneTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.SusceptibilityByGeneTemplate_definition, domain=SusceptibilityByGeneTemplate, range=Optional[str])

slots.SusceptibilityByGeneTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="SusceptibilityByGeneTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.SusceptibilityByGeneTemplate_equivalentTo, domain=SusceptibilityByGeneTemplate, range=Optional[str])

slots.OMIMDiseaseSeriesByGeneTemplate_disease = Slot(uri=DEFAULT_.disease, name="OMIMDiseaseSeriesByGeneTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.OMIMDiseaseSeriesByGeneTemplate_disease, domain=OMIMDiseaseSeriesByGeneTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.OMIMDiseaseSeriesByGeneTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="OMIMDiseaseSeriesByGeneTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.OMIMDiseaseSeriesByGeneTemplate_disease_label, domain=OMIMDiseaseSeriesByGeneTemplate, range=Optional[str])

slots.OMIMDiseaseSeriesByGeneTemplate_gene = Slot(uri=DEFAULT_.gene, name="OMIMDiseaseSeriesByGeneTemplate_gene", curie=DEFAULT_.curie('gene'),
                   model_uri=DEFAULT_.OMIMDiseaseSeriesByGeneTemplate_gene, domain=OMIMDiseaseSeriesByGeneTemplate, range=Optional[Union[str, GeneClassId]])

slots.OMIMDiseaseSeriesByGeneTemplate_gene_label = Slot(uri=DEFAULT_.gene_label, name="OMIMDiseaseSeriesByGeneTemplate_gene_label", curie=DEFAULT_.curie('gene_label'),
                   model_uri=DEFAULT_.OMIMDiseaseSeriesByGeneTemplate_gene_label, domain=OMIMDiseaseSeriesByGeneTemplate, range=Optional[str])

slots.OMIMDiseaseSeriesByGeneTemplate_name = Slot(uri=RDFS.label, name="OMIMDiseaseSeriesByGeneTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.OMIMDiseaseSeriesByGeneTemplate_name, domain=OMIMDiseaseSeriesByGeneTemplate, range=Optional[str])

slots.OMIMDiseaseSeriesByGeneTemplate_definition = Slot(uri=IAO['0000115'], name="OMIMDiseaseSeriesByGeneTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.OMIMDiseaseSeriesByGeneTemplate_definition, domain=OMIMDiseaseSeriesByGeneTemplate, range=Optional[str])

slots.OMIMDiseaseSeriesByGeneTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="OMIMDiseaseSeriesByGeneTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.OMIMDiseaseSeriesByGeneTemplate_equivalentTo, domain=OMIMDiseaseSeriesByGeneTemplate, range=Optional[str])

slots.AutoimmuneTemplate_disease = Slot(uri=DEFAULT_.disease, name="AutoimmuneTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.AutoimmuneTemplate_disease, domain=AutoimmuneTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.AutoimmuneTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="AutoimmuneTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.AutoimmuneTemplate_disease_label, domain=AutoimmuneTemplate, range=Optional[str])

slots.AutoimmuneTemplate_name = Slot(uri=RDFS.label, name="AutoimmuneTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AutoimmuneTemplate_name, domain=AutoimmuneTemplate, range=Optional[str])

slots.AutoimmuneTemplate_definition = Slot(uri=IAO['0000115'], name="AutoimmuneTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AutoimmuneTemplate_definition, domain=AutoimmuneTemplate, range=Optional[str])

slots.AutoimmuneTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AutoimmuneTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AutoimmuneTemplate_equivalentTo, domain=AutoimmuneTemplate, range=Optional[str])

slots.AdenomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="AdenomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.AdenomaDiseaseHasLocationXTemplate_location, domain=AdenomaDiseaseHasLocationXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.AdenomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="AdenomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.AdenomaDiseaseHasLocationXTemplate_location_label, domain=AdenomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.AdenomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="AdenomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AdenomaDiseaseHasLocationXTemplate_name, domain=AdenomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.AdenomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="AdenomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AdenomaDiseaseHasLocationXTemplate_definition, domain=AdenomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.AdenomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AdenomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AdenomaDiseaseHasLocationXTemplate_equivalentTo, domain=AdenomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.HereditaryTemplate_disease = Slot(uri=DEFAULT_.disease, name="HereditaryTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.HereditaryTemplate_disease, domain=HereditaryTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.HereditaryTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="HereditaryTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.HereditaryTemplate_disease_label, domain=HereditaryTemplate, range=Optional[str])

slots.HereditaryTemplate_name = Slot(uri=RDFS.label, name="HereditaryTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.HereditaryTemplate_name, domain=HereditaryTemplate, range=Optional[str])

slots.HereditaryTemplate_definition = Slot(uri=IAO['0000115'], name="HereditaryTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.HereditaryTemplate_definition, domain=HereditaryTemplate, range=Optional[str])

slots.HereditaryTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="HereditaryTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.HereditaryTemplate_equivalentTo, domain=HereditaryTemplate, range=Optional[str])

slots.JuvenileTemplate_disease = Slot(uri=DEFAULT_.disease, name="JuvenileTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.JuvenileTemplate_disease, domain=JuvenileTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.JuvenileTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="JuvenileTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.JuvenileTemplate_disease_label, domain=JuvenileTemplate, range=Optional[str])

slots.JuvenileTemplate_name = Slot(uri=RDFS.label, name="JuvenileTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.JuvenileTemplate_name, domain=JuvenileTemplate, range=Optional[str])

slots.JuvenileTemplate_definition = Slot(uri=IAO['0000115'], name="JuvenileTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.JuvenileTemplate_definition, domain=JuvenileTemplate, range=Optional[str])

slots.JuvenileTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="JuvenileTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.JuvenileTemplate_equivalentTo, domain=JuvenileTemplate, range=Optional[str])

slots.SquamousCellCarcinomaDiseaseHasLocationXTemplate_location = Slot(uri=DEFAULT_.location, name="SquamousCellCarcinomaDiseaseHasLocationXTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.SquamousCellCarcinomaDiseaseHasLocationXTemplate_location, domain=SquamousCellCarcinomaDiseaseHasLocationXTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.SquamousCellCarcinomaDiseaseHasLocationXTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="SquamousCellCarcinomaDiseaseHasLocationXTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.SquamousCellCarcinomaDiseaseHasLocationXTemplate_location_label, domain=SquamousCellCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.SquamousCellCarcinomaDiseaseHasLocationXTemplate_name = Slot(uri=RDFS.label, name="SquamousCellCarcinomaDiseaseHasLocationXTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.SquamousCellCarcinomaDiseaseHasLocationXTemplate_name, domain=SquamousCellCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.SquamousCellCarcinomaDiseaseHasLocationXTemplate_definition = Slot(uri=IAO['0000115'], name="SquamousCellCarcinomaDiseaseHasLocationXTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.SquamousCellCarcinomaDiseaseHasLocationXTemplate_definition, domain=SquamousCellCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.SquamousCellCarcinomaDiseaseHasLocationXTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="SquamousCellCarcinomaDiseaseHasLocationXTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.SquamousCellCarcinomaDiseaseHasLocationXTemplate_equivalentTo, domain=SquamousCellCarcinomaDiseaseHasLocationXTemplate, range=Optional[str])

slots.ExposureEventClass_subclass_of = Slot(uri=RDFS.subclass_of, name="ExposureEventClass_subclass_of", curie=RDFS.curie('subclass_of'),
                   model_uri=DEFAULT_.ExposureEventClass_subclass_of, domain=ExposureEventClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_disease = Slot(uri=DEFAULT_.disease, name="DiseaseRealizedInResponseToEnvironmentalExposureTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_disease, domain=DiseaseRealizedInResponseToEnvironmentalExposureTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="DiseaseRealizedInResponseToEnvironmentalExposureTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_disease_label, domain=DiseaseRealizedInResponseToEnvironmentalExposureTemplate, range=Optional[str])

slots.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_exposure = Slot(uri=DEFAULT_.exposure, name="DiseaseRealizedInResponseToEnvironmentalExposureTemplate_exposure", curie=DEFAULT_.curie('exposure'),
                   model_uri=DEFAULT_.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_exposure, domain=DiseaseRealizedInResponseToEnvironmentalExposureTemplate, range=Optional[Union[str, ExposureEventClassId]])

slots.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_exposure_label = Slot(uri=DEFAULT_.exposure_label, name="DiseaseRealizedInResponseToEnvironmentalExposureTemplate_exposure_label", curie=DEFAULT_.curie('exposure_label'),
                   model_uri=DEFAULT_.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_exposure_label, domain=DiseaseRealizedInResponseToEnvironmentalExposureTemplate, range=Optional[str])

slots.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_name = Slot(uri=RDFS.label, name="DiseaseRealizedInResponseToEnvironmentalExposureTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_name, domain=DiseaseRealizedInResponseToEnvironmentalExposureTemplate, range=Optional[str])

slots.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_definition = Slot(uri=IAO['0000115'], name="DiseaseRealizedInResponseToEnvironmentalExposureTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_definition, domain=DiseaseRealizedInResponseToEnvironmentalExposureTemplate, range=Optional[str])

slots.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="DiseaseRealizedInResponseToEnvironmentalExposureTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.DiseaseRealizedInResponseToEnvironmentalExposureTemplate_equivalentTo, domain=DiseaseRealizedInResponseToEnvironmentalExposureTemplate, range=Optional[str])

slots.SarcomaTemplate_location = Slot(uri=DEFAULT_.location, name="SarcomaTemplate_location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.SarcomaTemplate_location, domain=SarcomaTemplate, range=Optional[Union[str, OwlThingClassId]])

slots.SarcomaTemplate_location_label = Slot(uri=DEFAULT_.location_label, name="SarcomaTemplate_location_label", curie=DEFAULT_.curie('location_label'),
                   model_uri=DEFAULT_.SarcomaTemplate_location_label, domain=SarcomaTemplate, range=Optional[str])

slots.SarcomaTemplate_name = Slot(uri=RDFS.label, name="SarcomaTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.SarcomaTemplate_name, domain=SarcomaTemplate, range=Optional[str])

slots.SarcomaTemplate_definition = Slot(uri=IAO['0000115'], name="SarcomaTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.SarcomaTemplate_definition, domain=SarcomaTemplate, range=Optional[str])

slots.SarcomaTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="SarcomaTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.SarcomaTemplate_equivalentTo, domain=SarcomaTemplate, range=Optional[str])

slots.SyndromicTemplate_disease = Slot(uri=DEFAULT_.disease, name="SyndromicTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.SyndromicTemplate_disease, domain=SyndromicTemplate, range=Optional[Union[str, DiseaseOrDisorderClassId]])

slots.SyndromicTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="SyndromicTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.SyndromicTemplate_disease_label, domain=SyndromicTemplate, range=Optional[str])

slots.SyndromicTemplate_name = Slot(uri=RDFS.label, name="SyndromicTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.SyndromicTemplate_name, domain=SyndromicTemplate, range=Optional[str])

slots.SyndromicTemplate_definition = Slot(uri=IAO['0000115'], name="SyndromicTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.SyndromicTemplate_definition, domain=SyndromicTemplate, range=Optional[str])

slots.SyndromicTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="SyndromicTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.SyndromicTemplate_equivalentTo, domain=SyndromicTemplate, range=Optional[str])

slots.AutosomalRecessiveTemplate_disease = Slot(uri=DEFAULT_.disease, name="AutosomalRecessiveTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.AutosomalRecessiveTemplate_disease, domain=AutosomalRecessiveTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.AutosomalRecessiveTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="AutosomalRecessiveTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.AutosomalRecessiveTemplate_disease_label, domain=AutosomalRecessiveTemplate, range=Optional[str])

slots.AutosomalRecessiveTemplate_name = Slot(uri=RDFS.label, name="AutosomalRecessiveTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.AutosomalRecessiveTemplate_name, domain=AutosomalRecessiveTemplate, range=Optional[str])

slots.AutosomalRecessiveTemplate_definition = Slot(uri=IAO['0000115'], name="AutosomalRecessiveTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.AutosomalRecessiveTemplate_definition, domain=AutosomalRecessiveTemplate, range=Optional[str])

slots.AutosomalRecessiveTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="AutosomalRecessiveTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.AutosomalRecessiveTemplate_equivalentTo, domain=AutosomalRecessiveTemplate, range=Optional[str])

slots.RefractoryTemplate_disease = Slot(uri=DEFAULT_.disease, name="RefractoryTemplate_disease", curie=DEFAULT_.curie('disease'),
                   model_uri=DEFAULT_.RefractoryTemplate_disease, domain=RefractoryTemplate, range=Optional[Union[str, DiseaseClassId]])

slots.RefractoryTemplate_disease_label = Slot(uri=DEFAULT_.disease_label, name="RefractoryTemplate_disease_label", curie=DEFAULT_.curie('disease_label'),
                   model_uri=DEFAULT_.RefractoryTemplate_disease_label, domain=RefractoryTemplate, range=Optional[str])

slots.RefractoryTemplate_name = Slot(uri=RDFS.label, name="RefractoryTemplate_name", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.RefractoryTemplate_name, domain=RefractoryTemplate, range=Optional[str])

slots.RefractoryTemplate_definition = Slot(uri=IAO['0000115'], name="RefractoryTemplate_definition", curie=IAO.curie('0000115'),
                   model_uri=DEFAULT_.RefractoryTemplate_definition, domain=RefractoryTemplate, range=Optional[str])

slots.RefractoryTemplate_equivalentTo = Slot(uri=DEFAULT_.equivalentTo, name="RefractoryTemplate_equivalentTo", curie=DEFAULT_.curie('equivalentTo'),
                   model_uri=DEFAULT_.RefractoryTemplate_equivalentTo, domain=RefractoryTemplate, range=Optional[str])
