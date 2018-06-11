from typing import Dict, Any, Union


class Dataset:
    #dataset: Dict[Union[str, Any], Union[Union[str, Dict[str, str]], Any]]

    def __init__(self):
        self.dataset =  {
                    "principalInvestigator": "Francesco Piscitelli",
                    "endTime": "2018-06-07T09:46:27.560Z",
                    "creationLocation": "Multiblade",
                    "dataFormat": "lst",
                    "scientificMetadata": {"run":"1"},
                    "owner": "Francesco Piscitelli",
                    "ownerEmail": "francesco.piscitelli@esss.se",
                    "orcidOfOwner": "0000-0002-0325-4407",
                    "contactEmail": "francesco.piscitelli@esss.se",
                    "sourceFolder": "multiblade",
                    "proposalId": "2018ESS1",
                    "size": 102400,
                    "pid": "MB00001",
                    "packedSize": 1024000,
                    "creationTime": "2018-06-07T08:46:19.611Z",
                    "type": "raw",
                    "validationStatus": "valid",
                    "keywords": [
                        "Vanadium"
                    ],
                    "description": "string",
                    "userTargetLocation": "Multiblade",
                    "classification": "analyzed",
                    "license": "ESS",
                    "version": "v1",
                    "doi": "replace with doi",
                    "isPublished": True,
                    "ownerGroup": "brightness",
                    "accessGroups": [
                        "brightness"
                    ],
                    "createdBy": "ingestor",
                    "updatedBy": "ingestor",
                    "createdAt": "2018-06-07T08:46:19.611Z",
                    "updatedAt": "2018-06-07T08:46:19.611Z"
                }
