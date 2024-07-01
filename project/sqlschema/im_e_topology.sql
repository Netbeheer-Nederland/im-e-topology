-- # Class: "TopologicalNode" Description: "For a detailed substation model a topological node is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes change as the current network state changes (i.e., switches, breakers, etc. change state).For a planning model, switch statuses are not used to form topological nodes. Instead they are manually created or deleted in a model builder tool. Topological nodes maintained this way are also called "busses"."
--     * Slot: id Description: 
--     * Slot: description Description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
--     * Slot: energy_ident_code_eic Description: The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
--     * Slot: short_name Description: The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum.
--     * Slot: base_voltage_id Description: The base voltage of the topological node.
--     * Slot: connectivity_node_container_id Description: The connectivity node container to which the topological node belongs.
-- # Class: "BaseVoltage" Description: "Defines a system base voltage which is referenced."
--     * Slot: id Description: 
-- # Class: "ConnectivityNode" Description: "Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance."
--     * Slot: id Description: 
--     * Slot: topological_node_id Description: The topological node to which this connectivity node is assigned.  May depend on the current state of switches in the network.
-- # Class: "ConnectivityNodeContainer" Description: "A base class for all objects that may contain connectivity nodes or topological nodes."
--     * Slot: id Description: 
-- # Class: "Terminal" Description: "An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes."
--     * Slot: id Description: 
--     * Slot: description Description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
--     * Slot: energy_ident_code_eic Description: The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
--     * Slot: short_name Description: The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum.
--     * Slot: topological_node_id Description: The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unnecessary to model connectivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would probably not be used as an input specification.
-- # Class: "IdentifiedObject" Description: "This is a root class to provide common identification for all classes needing identification and naming attributes."
--     * Slot: id Description: 
--     * Slot: description Description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
--     * Slot: energy_ident_code_eic Description: The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
--     * Slot: short_name Description: The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum.
-- # Class: "ACDCTerminal" Description: "An electrical connection point (AC or DC) to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes."
--     * Slot: id Description: 
--     * Slot: description Description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
--     * Slot: energy_ident_code_eic Description: The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
--     * Slot: short_name Description: The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum.
-- # Class: "Name" Description: "The Name class provides the means to define any number of human readable  names for an object. A name is <b>not</b> to be used for defining inter-object relationships. For inter-object relationships instead use the object identification 'mRID'."
--     * Slot: id Description: 
--     * Slot: name_type_id Description: Type of this name.
--     * Slot: identified_object_id Description: Identified object that this name designates.
-- # Class: "NameType" Description: "Type of name. Possible values for attribute 'name' are implementation dependent but standard profiles may specify types. An enterprise may have multiple IT systems each having its own local name for the same object, e.g. a planning system may have different names from an EMS. An object may also have different names within the same IT system, e.g. localName as defined in CIM version 14. The definition from CIM14 is:The localName is a human readable name of the object. It is a free text name local to a node in a naming hierarchy similar to a file directory structure. A power system related naming hierarchy may be: Substation, VoltageLevel, Equipment etc. Children of the same parent in such a hierarchy have names that typically are unique among them."
--     * Slot: id Description: 
--     * Slot: description Description: Description of the name type.
--     * Slot: name_type_authority_id Description: Authority responsible for managing names of this type.
-- # Class: "NameTypeAuthority" Description: "Authority responsible for creation and management of names of a given type; typically an organization or an enterprise system."
--     * Slot: id Description: 
--     * Slot: description Description: Description of the name type authority.
-- # Class: "TopologicalNode_connectivity_nodes" Description: ""
--     * Slot: TopologicalNode_id Description: Autocreated FK slot
--     * Slot: connectivity_nodes_id Description: The connectivity nodes combine together to form this topological node.  May depend on the current state of switches in the network.
-- # Class: "TopologicalNode_terminal" Description: ""
--     * Slot: TopologicalNode_id Description: Autocreated FK slot
--     * Slot: terminal_id Description: The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unnecessary to model connectivity nodes in some cases.   Note that if connectivity nodes are in the model, this association would probably not be used as an input specification.
-- # Class: "TopologicalNode_names" Description: ""
--     * Slot: TopologicalNode_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this identified object.
-- # Class: "BaseVoltage_topological_node" Description: ""
--     * Slot: BaseVoltage_id Description: Autocreated FK slot
--     * Slot: topological_node_id Description: The topological nodes at the base voltage.
-- # Class: "ConnectivityNodeContainer_topological_node" Description: ""
--     * Slot: ConnectivityNodeContainer_id Description: Autocreated FK slot
--     * Slot: topological_node_id Description: The topological nodes which belong to this connectivity node container.
-- # Class: "Terminal_names" Description: ""
--     * Slot: Terminal_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this identified object.
-- # Class: "IdentifiedObject_names" Description: ""
--     * Slot: IdentifiedObject_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this identified object.
-- # Class: "ACDCTerminal_names" Description: ""
--     * Slot: ACDCTerminal_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this identified object.
-- # Class: "NameType_names" Description: ""
--     * Slot: NameType_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "NameTypeAuthority_name_types" Description: ""
--     * Slot: NameTypeAuthority_id Description: Autocreated FK slot
--     * Slot: name_types_id Description: All name types managed by this authority.

CREATE TABLE "BaseVoltage" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ConnectivityNodeContainer" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "IdentifiedObject" (
	id INTEGER NOT NULL, 
	description TEXT, 
	energy_ident_code_eic TEXT, 
	m_rid TEXT NOT NULL, 
	short_name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ACDCTerminal" (
	id INTEGER NOT NULL, 
	description TEXT, 
	energy_ident_code_eic TEXT, 
	m_rid TEXT NOT NULL, 
	short_name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "NameTypeAuthority" (
	id INTEGER NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TopologicalNode" (
	id INTEGER NOT NULL, 
	description TEXT, 
	energy_ident_code_eic TEXT, 
	m_rid TEXT NOT NULL, 
	short_name TEXT, 
	base_voltage_id INTEGER NOT NULL, 
	connectivity_node_container_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(base_voltage_id) REFERENCES "BaseVoltage" (id), 
	FOREIGN KEY(connectivity_node_container_id) REFERENCES "ConnectivityNodeContainer" (id)
);
CREATE TABLE "NameType" (
	id INTEGER NOT NULL, 
	description TEXT, 
	name_type_authority_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(name_type_authority_id) REFERENCES "NameTypeAuthority" (id)
);
CREATE TABLE "ConnectivityNode" (
	id INTEGER NOT NULL, 
	topological_node_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(topological_node_id) REFERENCES "TopologicalNode" (id)
);
CREATE TABLE "Terminal" (
	id INTEGER NOT NULL, 
	description TEXT, 
	energy_ident_code_eic TEXT, 
	m_rid TEXT NOT NULL, 
	short_name TEXT, 
	topological_node_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(topological_node_id) REFERENCES "TopologicalNode" (id)
);
CREATE TABLE "Name" (
	id INTEGER NOT NULL, 
	name_type_id INTEGER NOT NULL, 
	identified_object_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(name_type_id) REFERENCES "NameType" (id), 
	FOREIGN KEY(identified_object_id) REFERENCES "IdentifiedObject" (id)
);
CREATE TABLE "BaseVoltage_topological_node" (
	"BaseVoltage_id" INTEGER, 
	topological_node_id INTEGER, 
	PRIMARY KEY ("BaseVoltage_id", topological_node_id), 
	FOREIGN KEY("BaseVoltage_id") REFERENCES "BaseVoltage" (id), 
	FOREIGN KEY(topological_node_id) REFERENCES "TopologicalNode" (id)
);
CREATE TABLE "ConnectivityNodeContainer_topological_node" (
	"ConnectivityNodeContainer_id" INTEGER, 
	topological_node_id INTEGER, 
	PRIMARY KEY ("ConnectivityNodeContainer_id", topological_node_id), 
	FOREIGN KEY("ConnectivityNodeContainer_id") REFERENCES "ConnectivityNodeContainer" (id), 
	FOREIGN KEY(topological_node_id) REFERENCES "TopologicalNode" (id)
);
CREATE TABLE "NameTypeAuthority_name_types" (
	"NameTypeAuthority_id" INTEGER, 
	name_types_id INTEGER, 
	PRIMARY KEY ("NameTypeAuthority_id", name_types_id), 
	FOREIGN KEY("NameTypeAuthority_id") REFERENCES "NameTypeAuthority" (id), 
	FOREIGN KEY(name_types_id) REFERENCES "NameType" (id)
);
CREATE TABLE "TopologicalNode_connectivity_nodes" (
	"TopologicalNode_id" INTEGER, 
	connectivity_nodes_id INTEGER, 
	PRIMARY KEY ("TopologicalNode_id", connectivity_nodes_id), 
	FOREIGN KEY("TopologicalNode_id") REFERENCES "TopologicalNode" (id), 
	FOREIGN KEY(connectivity_nodes_id) REFERENCES "ConnectivityNode" (id)
);
CREATE TABLE "TopologicalNode_terminal" (
	"TopologicalNode_id" INTEGER, 
	terminal_id INTEGER NOT NULL, 
	PRIMARY KEY ("TopologicalNode_id", terminal_id), 
	FOREIGN KEY("TopologicalNode_id") REFERENCES "TopologicalNode" (id), 
	FOREIGN KEY(terminal_id) REFERENCES "Terminal" (id)
);
CREATE TABLE "TopologicalNode_names" (
	"TopologicalNode_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("TopologicalNode_id", names_id), 
	FOREIGN KEY("TopologicalNode_id") REFERENCES "TopologicalNode" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "Terminal_names" (
	"Terminal_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("Terminal_id", names_id), 
	FOREIGN KEY("Terminal_id") REFERENCES "Terminal" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "IdentifiedObject_names" (
	"IdentifiedObject_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("IdentifiedObject_id", names_id), 
	FOREIGN KEY("IdentifiedObject_id") REFERENCES "IdentifiedObject" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "ACDCTerminal_names" (
	"ACDCTerminal_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("ACDCTerminal_id", names_id), 
	FOREIGN KEY("ACDCTerminal_id") REFERENCES "ACDCTerminal" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "NameType_names" (
	"NameType_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("NameType_id", names_id), 
	FOREIGN KEY("NameType_id") REFERENCES "NameType" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);