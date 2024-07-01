# Auto generated from im_e_topology.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-07-01T11:07:38
# Schema: TopologyProfile
#
# id: http://data.netbeheernederland.nl/im-e-topology/version#1.0.0
# description: This vocabulary describes the topology profile from NBNLES.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CIM = CurieNamespace('cim', 'https://cim.ucaiug.io/ns#')
EU = CurieNamespace('eu', 'http://iec.ch/TC57/CIM100-European#')
GITHUB = CurieNamespace('github', 'https://github.com/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
THIS = CurieNamespace('this', 'http://data.netbeheernederland.nl/im-e-topology/def#')
DEFAULT_ = THIS


# Types

# Class references



@dataclass
class BaseVoltage(YAMLRoot):
    """
    Defines a system base voltage which is referenced.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["BaseVoltage"]
    class_class_curie: ClassVar[str] = "cim:BaseVoltage"
    class_name: ClassVar[str] = "BaseVoltage"
    class_model_uri: ClassVar[URIRef] = THIS.BaseVoltage

    topological_node: Optional[Union[Union[dict, "TopologicalNode"], List[Union[dict, "TopologicalNode"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="topological_node", slot_type=TopologicalNode, key_name="m_rid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ConnectivityNode(YAMLRoot):
    """
    Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero
    impedance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["ConnectivityNode"]
    class_class_curie: ClassVar[str] = "cim:ConnectivityNode"
    class_name: ClassVar[str] = "ConnectivityNode"
    class_model_uri: ClassVar[URIRef] = THIS.ConnectivityNode

    topological_node: Union[dict, "TopologicalNode"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.topological_node):
            self.MissingRequiredField("topological_node")
        if not isinstance(self.topological_node, TopologicalNode):
            self.topological_node = TopologicalNode(**as_dict(self.topological_node))

        super().__post_init__(**kwargs)


@dataclass
class ConnectivityNodeContainer(YAMLRoot):
    """
    A base class for all objects that may contain connectivity nodes or topological nodes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["ConnectivityNodeContainer"]
    class_class_curie: ClassVar[str] = "cim:ConnectivityNodeContainer"
    class_name: ClassVar[str] = "ConnectivityNodeContainer"
    class_model_uri: ClassVar[URIRef] = THIS.ConnectivityNodeContainer

    topological_node: Optional[Union[Union[dict, "TopologicalNode"], List[Union[dict, "TopologicalNode"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="topological_node", slot_type=TopologicalNode, key_name="m_rid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class IdentifiedObject(YAMLRoot):
    """
    This is a root class to provide common identification for all classes needing identification and naming attributes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["IdentifiedObject"]
    class_class_curie: ClassVar[str] = "cim:IdentifiedObject"
    class_name: ClassVar[str] = "IdentifiedObject"
    class_model_uri: ClassVar[URIRef] = THIS.IdentifiedObject

    m_rid: str = None
    description: Optional[str] = None
    energy_ident_code_eic: Optional[str] = None
    short_name: Optional[str] = None
    names: Optional[Union[Union[dict, "Name"], List[Union[dict, "Name"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.m_rid):
            self.MissingRequiredField("m_rid")
        if not isinstance(self.m_rid, str):
            self.m_rid = str(self.m_rid)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.energy_ident_code_eic is not None and not isinstance(self.energy_ident_code_eic, str):
            self.energy_ident_code_eic = str(self.energy_ident_code_eic)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        self._normalize_inlined_as_dict(slot_name="names", slot_type=Name, key_name="name_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class TopologicalNode(IdentifiedObject):
    """
    For a detailed substation model a topological node is a set of connectivity nodes that, in the current network
    state, are connected together through any type of closed switches, including jumpers. Topological nodes change as
    the current network state changes (i.e., switches, breakers, etc. change state).
    For a planning model, switch statuses are not used to form topological nodes. Instead they are manually created or
    deleted in a model builder tool. Topological nodes maintained this way are also called "busses".
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["TopologicalNode"]
    class_class_curie: ClassVar[str] = "cim:TopologicalNode"
    class_name: ClassVar[str] = "TopologicalNode"
    class_model_uri: ClassVar[URIRef] = THIS.TopologicalNode

    m_rid: str = None
    base_voltage: Union[dict, BaseVoltage] = None
    connectivity_node_container: Union[dict, ConnectivityNodeContainer] = None
    terminal: Union[Union[dict, "Terminal"], List[Union[dict, "Terminal"]]] = None
    connectivity_nodes: Optional[Union[Union[dict, ConnectivityNode], List[Union[dict, ConnectivityNode]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.base_voltage):
            self.MissingRequiredField("base_voltage")
        if not isinstance(self.base_voltage, BaseVoltage):
            self.base_voltage = BaseVoltage(**as_dict(self.base_voltage))

        if self._is_empty(self.connectivity_node_container):
            self.MissingRequiredField("connectivity_node_container")
        if not isinstance(self.connectivity_node_container, ConnectivityNodeContainer):
            self.connectivity_node_container = ConnectivityNodeContainer(**as_dict(self.connectivity_node_container))

        if self._is_empty(self.terminal):
            self.MissingRequiredField("terminal")
        self._normalize_inlined_as_dict(slot_name="terminal", slot_type=Terminal, key_name="m_rid", keyed=False)

        self._normalize_inlined_as_dict(slot_name="connectivity_nodes", slot_type=ConnectivityNode, key_name="topological_node", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ACDCTerminal(IdentifiedObject):
    """
    An electrical connection point (AC or DC) to a piece of conducting equipment. Terminals are connected at physical
    connection points called connectivity nodes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["ACDCTerminal"]
    class_class_curie: ClassVar[str] = "cim:ACDCTerminal"
    class_name: ClassVar[str] = "ACDCTerminal"
    class_model_uri: ClassVar[URIRef] = THIS.ACDCTerminal

    m_rid: str = None

@dataclass
class Terminal(ACDCTerminal):
    """
    An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical
    connection points called connectivity nodes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["Terminal"]
    class_class_curie: ClassVar[str] = "cim:Terminal"
    class_name: ClassVar[str] = "Terminal"
    class_model_uri: ClassVar[URIRef] = THIS.Terminal

    m_rid: str = None
    topological_node: Optional[Union[dict, TopologicalNode]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.topological_node is not None and not isinstance(self.topological_node, TopologicalNode):
            self.topological_node = TopologicalNode(**as_dict(self.topological_node))

        super().__post_init__(**kwargs)


@dataclass
class Name(YAMLRoot):
    """
    The Name class provides the means to define any number of human readable names for an object. A name is <b>not</b>
    to be used for defining inter-object relationships. For inter-object relationships instead use the object
    identification 'mRID'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["Name"]
    class_class_curie: ClassVar[str] = "cim:Name"
    class_name: ClassVar[str] = "Name"
    class_model_uri: ClassVar[URIRef] = THIS.Name

    name_type: Union[dict, "NameType"] = None
    identified_object: Union[dict, IdentifiedObject] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name_type):
            self.MissingRequiredField("name_type")
        if not isinstance(self.name_type, NameType):
            self.name_type = NameType(**as_dict(self.name_type))

        if self._is_empty(self.identified_object):
            self.MissingRequiredField("identified_object")
        if not isinstance(self.identified_object, IdentifiedObject):
            self.identified_object = IdentifiedObject(**as_dict(self.identified_object))

        super().__post_init__(**kwargs)


@dataclass
class NameType(YAMLRoot):
    """
    Type of name. Possible values for attribute 'name' are implementation dependent but standard profiles may specify
    types. An enterprise may have multiple IT systems each having its own local name for the same object, e.g. a
    planning system may have different names from an EMS. An object may also have different names within the same IT
    system, e.g. localName as defined in CIM version 14. The definition from CIM14 is:
    The localName is a human readable name of the object. It is a free text name local to a node in a naming hierarchy
    similar to a file directory structure. A power system related naming hierarchy may be: Substation, VoltageLevel,
    Equipment etc. Children of the same parent in such a hierarchy have names that typically are unique among them.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["NameType"]
    class_class_curie: ClassVar[str] = "cim:NameType"
    class_name: ClassVar[str] = "NameType"
    class_model_uri: ClassVar[URIRef] = THIS.NameType

    description: Optional[str] = None
    name_type_authority: Optional[Union[dict, "NameTypeAuthority"]] = None
    names: Optional[Union[Union[dict, Name], List[Union[dict, Name]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.name_type_authority is not None and not isinstance(self.name_type_authority, NameTypeAuthority):
            self.name_type_authority = NameTypeAuthority(**as_dict(self.name_type_authority))

        self._normalize_inlined_as_dict(slot_name="names", slot_type=Name, key_name="name_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class NameTypeAuthority(YAMLRoot):
    """
    Authority responsible for creation and management of names of a given type; typically an organization or an
    enterprise system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["NameTypeAuthority"]
    class_class_curie: ClassVar[str] = "cim:NameTypeAuthority"
    class_name: ClassVar[str] = "NameTypeAuthority"
    class_model_uri: ClassVar[URIRef] = THIS.NameTypeAuthority

    description: Optional[str] = None
    name_types: Optional[Union[Union[dict, NameType], List[Union[dict, NameType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.name_types, list):
            self.name_types = [self.name_types] if self.name_types is not None else []
        self.name_types = [v if isinstance(v, NameType) else NameType(**as_dict(v)) for v in self.name_types]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.topologicalNode__base_voltage = Slot(uri=CIM['TopologicalNode.BaseVoltage'], name="topologicalNode__base_voltage", curie=CIM.curie('TopologicalNode.BaseVoltage'),
                   model_uri=THIS.topologicalNode__base_voltage, domain=None, range=Union[dict, BaseVoltage])

slots.topologicalNode__connectivity_nodes = Slot(uri=CIM['TopologicalNode.ConnectivityNodes'], name="topologicalNode__connectivity_nodes", curie=CIM.curie('TopologicalNode.ConnectivityNodes'),
                   model_uri=THIS.topologicalNode__connectivity_nodes, domain=None, range=Optional[Union[Union[dict, ConnectivityNode], List[Union[dict, ConnectivityNode]]]])

slots.topologicalNode__connectivity_node_container = Slot(uri=CIM['TopologicalNode.ConnectivityNodeContainer'], name="topologicalNode__connectivity_node_container", curie=CIM.curie('TopologicalNode.ConnectivityNodeContainer'),
                   model_uri=THIS.topologicalNode__connectivity_node_container, domain=None, range=Union[dict, ConnectivityNodeContainer])

slots.topologicalNode__terminal = Slot(uri=CIM['TopologicalNode.Terminal'], name="topologicalNode__terminal", curie=CIM.curie('TopologicalNode.Terminal'),
                   model_uri=THIS.topologicalNode__terminal, domain=None, range=Union[Union[dict, Terminal], List[Union[dict, Terminal]]])

slots.baseVoltage__topological_node = Slot(uri=CIM['BaseVoltage.TopologicalNode'], name="baseVoltage__topological_node", curie=CIM.curie('BaseVoltage.TopologicalNode'),
                   model_uri=THIS.baseVoltage__topological_node, domain=None, range=Optional[Union[Union[dict, TopologicalNode], List[Union[dict, TopologicalNode]]]])

slots.connectivityNode__topological_node = Slot(uri=CIM['ConnectivityNode.TopologicalNode'], name="connectivityNode__topological_node", curie=CIM.curie('ConnectivityNode.TopologicalNode'),
                   model_uri=THIS.connectivityNode__topological_node, domain=None, range=Union[dict, TopologicalNode])

slots.connectivityNodeContainer__topological_node = Slot(uri=CIM['ConnectivityNodeContainer.TopologicalNode'], name="connectivityNodeContainer__topological_node", curie=CIM.curie('ConnectivityNodeContainer.TopologicalNode'),
                   model_uri=THIS.connectivityNodeContainer__topological_node, domain=None, range=Optional[Union[Union[dict, TopologicalNode], List[Union[dict, TopologicalNode]]]])

slots.terminal__topological_node = Slot(uri=CIM['Terminal.TopologicalNode'], name="terminal__topological_node", curie=CIM.curie('Terminal.TopologicalNode'),
                   model_uri=THIS.terminal__topological_node, domain=None, range=Optional[Union[dict, TopologicalNode]])

slots.identifiedObject__description = Slot(uri=CIM['IdentifiedObject.description'], name="identifiedObject__description", curie=CIM.curie('IdentifiedObject.description'),
                   model_uri=THIS.identifiedObject__description, domain=None, range=Optional[str])

slots.identifiedObject__energy_ident_code_eic = Slot(uri=EU['IdentifiedObject.energyIdentCodeEic'], name="identifiedObject__energy_ident_code_eic", curie=EU.curie('IdentifiedObject.energyIdentCodeEic'),
                   model_uri=THIS.identifiedObject__energy_ident_code_eic, domain=None, range=Optional[str])

slots.identifiedObject__m_rid = Slot(uri=CIM['IdentifiedObject.mRID'], name="identifiedObject__m_rid", curie=CIM.curie('IdentifiedObject.mRID'),
                   model_uri=THIS.identifiedObject__m_rid, domain=None, range=str)

slots.identifiedObject__short_name = Slot(uri=EU['IdentifiedObject.shortName'], name="identifiedObject__short_name", curie=EU.curie('IdentifiedObject.shortName'),
                   model_uri=THIS.identifiedObject__short_name, domain=None, range=Optional[str])

slots.identifiedObject__names = Slot(uri=CIM['IdentifiedObject.Names'], name="identifiedObject__names", curie=CIM.curie('IdentifiedObject.Names'),
                   model_uri=THIS.identifiedObject__names, domain=None, range=Optional[Union[Union[dict, Name], List[Union[dict, Name]]]])

slots.name__name_type = Slot(uri=CIM['Name.NameType'], name="name__name_type", curie=CIM.curie('Name.NameType'),
                   model_uri=THIS.name__name_type, domain=None, range=Union[dict, NameType])

slots.name__identified_object = Slot(uri=CIM['Name.IdentifiedObject'], name="name__identified_object", curie=CIM.curie('Name.IdentifiedObject'),
                   model_uri=THIS.name__identified_object, domain=None, range=Union[dict, IdentifiedObject])

slots.nameType__description = Slot(uri=CIM['NameType.description'], name="nameType__description", curie=CIM.curie('NameType.description'),
                   model_uri=THIS.nameType__description, domain=None, range=Optional[str])

slots.nameType__name_type_authority = Slot(uri=CIM['NameType.NameTypeAuthority'], name="nameType__name_type_authority", curie=CIM.curie('NameType.NameTypeAuthority'),
                   model_uri=THIS.nameType__name_type_authority, domain=None, range=Optional[Union[dict, NameTypeAuthority]])

slots.nameType__names = Slot(uri=CIM['NameType.Names'], name="nameType__names", curie=CIM.curie('NameType.Names'),
                   model_uri=THIS.nameType__names, domain=None, range=Optional[Union[Union[dict, Name], List[Union[dict, Name]]]])

slots.nameTypeAuthority__description = Slot(uri=CIM['NameTypeAuthority.description'], name="nameTypeAuthority__description", curie=CIM.curie('NameTypeAuthority.description'),
                   model_uri=THIS.nameTypeAuthority__description, domain=None, range=Optional[str])

slots.nameTypeAuthority__name_types = Slot(uri=CIM['NameTypeAuthority.NameTypes'], name="nameTypeAuthority__name_types", curie=CIM.curie('NameTypeAuthority.NameTypes'),
                   model_uri=THIS.nameTypeAuthority__name_types, domain=None, range=Optional[Union[Union[dict, NameType], List[Union[dict, NameType]]]])