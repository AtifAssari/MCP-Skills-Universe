---
title: pdb
url: https://skills.sh/adaptyvbio/protein-design-skills/pdb
---

# pdb

skills/adaptyvbio/protein-design-skills/pdb
pdb
Installation
$ npx skills add https://github.com/adaptyvbio/protein-design-skills --skill pdb
SKILL.md
PDB Database Access

Note: This skill uses the RCSB PDB web API directly. No Modal deployment needed - all operations run locally via HTTP requests.

Fetching Structures
By PDB ID
# Download PDB file
curl -o 1alu.pdb "https://files.rcsb.org/download/1ALU.pdb"

# Download mmCIF
curl -o 1alu.cif "https://files.rcsb.org/download/1ALU.cif"

Using Python
from Bio.PDB import PDBList

pdbl = PDBList()
pdbl.retrieve_pdb_file("1ABC", pdir="structures/", file_format="pdb")

Using RCSB API
import requests

def fetch_pdb(pdb_id: str, format: str = "pdb") -> str:
    """Fetch structure from RCSB PDB."""
    url = f"https://files.rcsb.org/download/{pdb_id}.{format}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def fetch_fasta(pdb_id: str) -> str:
    """Fetch sequence in FASTA format."""
    url = f"https://www.rcsb.org/fasta/entry/{pdb_id}"
    return requests.get(url).text

# Example usage
pdb_content = fetch_pdb("1ALU")
with open("1ALU.pdb", "w") as f:
    f.write(pdb_content)

Structure Preparation
Selecting Chains
from Bio.PDB import PDBParser, PDBIO, Select

class ChainSelect(Select):
    def __init__(self, chain_id):
        self.chain_id = chain_id

    def accept_chain(self, chain):
        return chain.id == self.chain_id

# Extract chain A
parser = PDBParser()
structure = parser.get_structure("protein", "1abc.pdb")
io = PDBIO()
io.set_structure(structure)
io.save("chain_A.pdb", ChainSelect("A"))

Trimming to Binding Region
def trim_around_residues(pdb_file, center_residues, buffer=10.0):
    """Trim structure to region around specified residues."""
    parser = PDBParser()
    structure = parser.get_structure("protein", pdb_file)

    # Get center coordinates
    center_coords = []
    for res in structure.get_residues():
        if res.id[1] in center_residues:
            center_coords.extend([a.coord for a in res.get_atoms()])

    center = np.mean(center_coords, axis=0)

    # Keep residues within buffer
    class RegionSelect(Select):
        def accept_residue(self, res):
            for atom in res.get_atoms():
                if np.linalg.norm(atom.coord - center) < buffer:
                    return True
            return False

    io = PDBIO()
    io.set_structure(structure)
    io.save("trimmed.pdb", RegionSelect())

Searching PDB
RCSB Search API
import requests

query = {
    "query": {
        "type": "terminal",
        "service": "full_text",
        "parameters": {
            "value": "EGFR kinase domain"
        }
    },
    "return_type": "entry"
}

response = requests.post(
    "https://search.rcsb.org/rcsbsearch/v2/query",
    json=query
)
results = response.json()

By Sequence Similarity
query = {
    "query": {
        "type": "terminal",
        "service": "sequence",
        "parameters": {
            "value": "MKTAYIAKQRQISFVK...",
            "evalue_cutoff": 1e-10,
            "identity_cutoff": 0.9
        }
    }
}

Structure Analysis
Get Chain Info
def get_structure_info(pdb_file):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("protein", pdb_file)

    info = {
        "chains": [],
        "total_residues": 0
    }

    for model in structure:
        for chain in model:
            residues = list(chain.get_residues())
            info["chains"].append({
                "id": chain.id,
                "length": len(residues),
                "first_res": residues[0].id[1],
                "last_res": residues[-1].id[1]
            })
            info["total_residues"] += len(residues)

    return info

Find Interface Residues
def find_interface_residues(pdb_file, chain_a, chain_b, distance=4.0):
    """Find residues at interface between two chains."""
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("complex", pdb_file)

    interface_a = set()
    interface_b = set()

    for res_a in structure[0][chain_a].get_residues():
        for res_b in structure[0][chain_b].get_residues():
            for atom_a in res_a.get_atoms():
                for atom_b in res_b.get_atoms():
                    if atom_a - atom_b < distance:
                        interface_a.add(res_a.id[1])
                        interface_b.add(res_b.id[1])

    return interface_a, interface_b

Common Tasks for Binder Design
Target Preparation Checklist
Download structure: curl -o target.pdb "https://files.rcsb.org/download/XXXX.pdb"
Identify target chain
Remove waters and ligands (if needed)
Trim to binding region + buffer
Identify potential hotspots
Renumber if needed
Troubleshooting

Structure not found: Check PDB ID format (4 characters) Multiple models: Select first model for design Missing residues: Check for gaps in structure

Next: Use structure with boltzgen (recommended) or rfdiffusion for design.

Weekly Installs
23
Repository
adaptyvbio/prot…n-skills
GitHub Stars
125
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass