import requests
from maltego_trx.transform import DiscoverableTransform


class DomainToCertificates(DiscoverableTransform):
    """
    Class to populate a custom entity called Certificates
    with relevant certificate information from a given url
    """
    base_url = "https://crt.sh/"

    @classmethod
    def get_response(cls, domain_name, maltego_response):
        """
        :param domain_name:
        :param maltego_response:
        :return:
        """
        # ?CN=maltego.com&output=json
        response = requests.get(cls.base_url, params={
            "CN": domain_name,
            "output": "json"
        })
        if response.status_code == 200:
            return cls.format_response(response.json(), maltego_response)
        maltego_response.addUIMessage("crt.sh server replied with: {}".format(response.text))

    @classmethod
    def format_response(cls, json_response, maltego_response):
        """
        Sample dict inside response:
        issuer_ca_id	183267
        issuer_name	"C=US, O=Let's Encrypt, CN=R3"
        name_value	"maltego.com"
        id	4114515069
        entry_timestamp	"2021-02-22T04:00:41.343"
        not_before	"2021-02-22T03:00:40"
        not_after	"2021-05-23T03:00:40"
        serial_number	"03bf02afa25984c2208f8e72dcdc839f857e"

        :param json_response:
        :param maltego_response:
        :return:
        """
        for certificate_dict in json_response:
            entity = maltego_response.addEntity(
                "certificate_information",
                certificate_dict.get("name_value", "")
            )
            entity.addProperty(
                "properties.certificate",
                displayName="ID of the Certificate",
                value=certificate_dict.get("id", "")
            )
            entity.addProperty(
                "issuer_name",
                displayName="Name of the issuer",
                value=certificate_dict.get("issuer_name", "")
            )
            entity.addProperty(
                "issuer_id",
                displayName="Name of the issuer",
                value=certificate_dict.get("issuer_ca_id", "")
            )
            entity.addProperty(
                "expiry_date",
                displayName="Expiry Date",
                value=certificate_dict.get("not_after", "")
            )
            entity.addProperty(
                "subject",
                displayName="Subject",
                value=certificate_dict.get("name_value", "")
            )

    @classmethod
    def create_entities(cls, request, response):
        """
        :param request:
        :param response:
        :return:
        """
        domain_name = request.Value
        cls.get_response(domain_name, response)
