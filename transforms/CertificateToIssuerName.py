from maltego_trx.entities import Phrase
from maltego_trx.transform import DiscoverableTransform


class CertificateToIssuerName(DiscoverableTransform):
    """
    Display the name of the certificate
    """

    @classmethod
    def get_cname(cls, issuer_phrase: str, maltego_response):
        tokens = issuer_phrase.split("CN=")
        try:
            return tokens[-1]
        except IndexError as ie:
            maltego_response.addUIMessage(ie)
            return ""

    @classmethod
    def create_entities(cls, request, response):
        """
        :param request:
        :param response:
        :return:
        """
        issuer_phrase = request.getProperty("issuer_name")
        issuer_name = cls.get_cname(issuer_phrase, response)
        if issuer_name:
            response.addEntity(Phrase, value=issuer_name)
