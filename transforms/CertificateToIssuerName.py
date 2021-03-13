from maltego_trx.entities import Phrase
from maltego_trx.transform import DiscoverableTransform


class CertificateToIssuerName(DiscoverableTransform):
    """
    Display the name of the certificate
    """

    @classmethod
    def get_cname(cls, issuer_phrase: str):
        tokens = issuer_phrase.split(",")
        final_token = tokens[-1]
        return final_token.split("=")[-1]

    @classmethod
    def create_entities(cls, request, response):
        """
        :param request:
        :param response:
        :return:
        """
        issuer_phrase = request.getProperty("issuer_name")
        response.addEntity(Phrase, value=cls.get_cname(issuer_phrase))
