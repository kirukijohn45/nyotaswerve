"""
Tally Prime XML API client.
Tally listens on HTTP port 9000 by default and communicates via XML.
"""

import logging
import xml.etree.ElementTree as ET
from urllib import request as url_request
from urllib.error import URLError
from django.conf import settings

logger = logging.getLogger(__name__)


class TallyClient:
    """Client for communicating with Tally Prime via XML API."""
    
    def __init__(self, host=None, port=None, timeout=None):
        config = settings.TALLY_CONFIG
        self.host = host or config['HOST']
        self.port = port or config['PORT']
        self.timeout = timeout or config['TIMEOUT']
        self.url = f'http://{self.host}:{self.port}'
    
    def send_request(self, xml_payload):
        """Send XML request to Tally and return response."""
        headers = {'Content-Type': 'application/xml'}
        data = xml_payload.encode('utf-8')
        
        try:
            req = url_request.Request(self.url, data=data, headers=headers, method='POST')
            with url_request.urlopen(req, timeout=self.timeout) as resp:
                return resp.read().decode('utf-8')
        except URLError as e:
            logger.error(f'Tally connection failed: {e}')
            raise ConnectionError(f'Cannot connect to Tally at {self.url}: {e}')
        except Exception as e:
            logger.error(f'Tally request failed: {e}')
            raise
    
    def get_ledgers(self):
        """Fetch all ledgers from Tally."""
        xml = f"""<ENVELOPE>
            <HEADER>
                <TALLYREQUEST>Export Data</TALLYREQUEST>
            </HEADER>
            <BODY>
                <EXPORTDATA>
                    <REQUESTDESC>
                        <REPORTNAME>Ledger</REPORTNAME>
                        <STATICVARIABLES>
                            <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                        </STATICVARIABLES>
                    </REQUESTDESC>
                </EXPORTDATA>
            </BODY>
        </ENVELOPE>"""
        return self.send_request(xml)
    
    def get_stock_items(self):
        """Fetch all stock items from Tally."""
        xml = f"""<ENVELOPE>
            <HEADER>
                <TALLYREQUEST>Export Data</TALLYREQUEST>
            </HEADER>
            <BODY>
                <EXPORTDATA>
                    <REQUESTDESC>
                        <REPORTNAME>Stock Item</REPORTNAME>
                        <STATICVARIABLES>
                            <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                        </STATICVARIABLES>
                    </REQUESTDESC>
                </EXPORTDATA>
            </BODY>
        </ENVELOPE>"""
        return self.send_request(xml)
    
    def create_ledger(self, name, parent_group='Sundry Debtors', 
                      mailing_name=None, address=None, 
                      city=None, state=None, pincode=None,
                      phone=None, email=None):
        """Create a ledger in Tally Prime."""
        
        mailing_name = mailing_name or name
        address = address or ''
        city = city or ''
        state = state or ''
        pincode = pincode or ''
        phone = phone or ''
        email = email or ''
        
        xml = f"""<ENVELOPE>
            <HEADER>
                <TALLYREQUEST>Import Data</TALLYREQUEST>
            </HEADER>
            <BODY>
                <IMPORTDATA>
                    <REQUESTDESC>
                        <REPORTNAME>All Masters</REPORTNAME>
                        <STATICVARIABLES>
                            <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                        </STATICVARIABLES>
                    </REQUESTDESC>
                    <REQUESTDATA>
                        <TALLYMESSAGE xmlns:UDF="TallyUDF">
                            <LEDGER NAME="{name}" ACTION="Create">
                                <NAME.LIST>
                                    <NAME>{name}</NAME>
                                </NAME.LIST>
                                <PARENT>{parent_group}</PARENT>
                                <ISACTIVE>Yes</ISACTIVE>
                                <LANGUAGENAME.LIST>
                                    <NAME.LIST>
                                        <NAME>{name}</NAME>
                                    </NAME.LIST>
                                    <LANGUAGEID>1033</LANGUAGEID>
                                </LANGUAGENAME.LIST>
                                <MAILLINGNAME.LIST>
                                    <MAILLINGNAME>{mailing_name}</MAILLINGNAME>
                                </MAILLINGNAME.LIST>
                                <ADDRESS.LIST>
                                    <ADDRESS>{address}</ADDRESS>
                                    <CITY>{city}</CITY>
                                    <STATE>{state}</STATE>
                                    <PINCODE>{pincode}</PINCODE>
                                    <COUNTRY/>
                                </ADDRESS.LIST>
                                <PHONE>{phone}</PHONE>
                                <EMAIL>{email}</EMAIL>
                                <LEDGERPHOTO/>
                            </LEDGER>
                        </TALLYMESSAGE>
                    </REQUESTDATA>
                </IMPORTDATA>
            </BODY>
        </ENVELOPE>"""
        return self.send_request(xml)
    
    def create_sales_voucher(self, voucher_no, date, party_ledger_name,
                             items, amount, currency='KES'):
        """Create a sales voucher in Tally Prime."""
        
        # Build voucher items XML
        items_xml = ''
        for i, item in enumerate(items, 1):
            items_xml += f"""<ALLINVENTORYENTRIES.LIST>
                    <BASICRATE.LIST>
                        <RATE>{item['rate']}</RATE>
                    </BASICRATE.LIST>
                    <RATE>{item['rate']}</RATE>
                    <AMOUNT>{item['amount']}</AMOUNT>
                    <STOCKITEMNAME>{item['stock_name']}</STOCKITEMNAME>
                    <BATCHALLOCATIONS.LIST>
                        <GODOWNNAME>Main Location</GODOWNNAME>
                        <ACTUALQTY>{item['quantity']}</ACTUALQTY>
                    </BATCHALLOCATIONS.LIST>
                    <ACTUALQTY>{item['quantity']}</ACTUALQTY>
                    <BILLEDQTY>{item['quantity']}</BILLEDQTY>
                </ALLINVENTORYENTRIES.LIST>"""
        
        xml = f"""<ENVELOPE>
            <HEADER>
                <TALLYREQUEST>Import Data</TALLYREQUEST>
            </HEADER>
            <BODY>
                <IMPORTDATA>
                    <REQUESTDESC>
                        <REPORTNAME>All Masters</REPORTNAME>
                        <STATICVARIABLES>
                            <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                        </STATICVARIABLES>
                    </REQUESTDESC>
                    <REQUESTDATA>
                        <TALLYMESSAGE xmlns:UDF="TallyUDF">
                            <VOUCHER ACTION="Create" VCHTYPE="Sales">
                                <VOUCHERNUMBER>{voucher_no}</VOUCHERNUMBER>
                                <DATE>{date}</DATE>
                                <PARTYLEDGERNAME>{party_ledger_name}</PARTYLEDGERNAME>
                                <PERSISTEDVIEW>Invoice</PERSISTEDVIEW>
                                <VCHGSTCLASS/>
                                <ISGOVCHALLAN>No</ISGOVCHALLAN>
                                <ASPAYSLIP>No</ASPAYSLIP>
                                <ISTDSONPAYSLIP>No</ISTDSONPAYSLIP>
                                <ISITEMBILLEDFORPACKING>No</ISITEMBILLEDFORPACKING>
                                <VOUCHERTYPEVCHNAME>Sales</VOUCHERTYPEVCHNAME>
                                <DATEOFBILLING>{date}</DATEOFBILLING>
                                {items_xml}
                                <LEDGERENTRIES.LIST>
                                    <LEDGERNAME>{party_ledger_name}</LEDGERNAME>
                                    <ISDEEMEDPOSITIVE>Yes</ISDEEMEDPOSITIVE>
                                    <AMOUNT>{amount}</AMOUNT>
                                </LEDGERENTRIES.LIST>
                            </VOUCHER>
                        </TALLYMESSAGE>
                    </REQUESTDATA>
                </IMPORTDATA>
            </BODY>
        </ENVELOPE>"""
        return self.send_request(xml)
    
    def test_connection(self):
        """Test if Tally Prime is reachable."""
        try:
            self.get_ledgers()
            return True, 'Connected successfully'
        except ConnectionError as e:
            return False, str(e)
        except Exception as e:
            return False, f'Error: {str(e)}'