from dataclasses import dataclass

from solidpy_domain.common.dataclass.person import Person, Organization


@dataclass
class Survey:
    id: str
    name: str
    description: str
    owner: Organization
    participants: [Person]
