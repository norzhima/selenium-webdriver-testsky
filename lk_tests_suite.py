# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
#import HtmlTestRunner
import os
from lk_test_auth import TestAuth
from lk_test_cashin_advcash import TestCashInAdvcash
from lk_test_cashin_ameria import TestCashInAmeria
from lk_test_cashin_bitcoin import TestCashInBitcoin
from lk_test_cashin_cryptonator import TestCashInCryptonator
from lk_test_cashin_fasapay import TestCashInFasapay
from lk_test_cashin_impex import TestCashInImpex
# from lk_old_test_cashin_megapolis import TestCashInMegapolis
# from lk_old_test_cashin_megapolis_agree import TestCashInMegapolisAgree
from lk_test_cashin_mera import TestCashInMera
from lk_test_cashin_pm import TestCashInPm
# from lk_old_test_cashin_swift import TestCashInSwift
# from lk_old_test_cashin_tinkoff import TestCashInTinkoff
# from lk_old_test_cashin_tinkoff_agree import TestCashInTinkoffAgree
from lk_test_cashin_tt_swift import TestCashInTtswift
from lk_test_cashin_webmoney import TestCashInWebmoney
from lk_test_packet_instalment_500 import TestsPacketInstalment500
from lk_test_packet_instalment_start import TestsPacketInstalmentStart
from lk_test_packet_instalment_start_plus import TestsPacketInstalmentStartPlus
from lk_test_packet_simple_premium_5000 import TestsPacketSimplePremium5000
from lk_test_registration import TestRegistration
from lk_test_transfer_of_money import TestTransferOfMoney
from lk_test_verification import TestVerification
from lk_test_withdrawal_request import TestWithdrawalRequest

test_auth = unittest.TestLoader().loadTestsFromTestCase(TestAuth)
tests_cashin_advcash = unittest.TestLoader().loadTestsFromTestCase(TestCashInAdvcash)
test_cashin_ameria = unittest.TestLoader().loadTestsFromTestCase(TestCashInAmeria)
test_cashin_bitcoin = unittest.TestLoader().loadTestsFromTestCase(TestCashInBitcoin)
tests_cashin_cryptonator = unittest.TestLoader().loadTestsFromTestCase(TestCashInCryptonator)
test_cashin_fasapay = unittest.TestLoader().loadTestsFromTestCase(TestCashInFasapay)
tests_cashin_impex = unittest.TestLoader().loadTestsFromTestCase(TestCashInImpex)
tests_cashin_mera = unittest.TestLoader().loadTestsFromTestCase(TestCashInMera)
test_cashin_pm = unittest.TestLoader().loadTestsFromTestCase(TestCashInPm)
test_cashin_webmoney = unittest.TestLoader().loadTestsFromTestCase(TestCashInWebmoney)
test_packet_instalment_500 = unittest.TestLoader().loadTestsFromTestCase(TestsPacketInstalment500)
test_packet_instalment_start = unittest.TestLoader().loadTestsFromTestCase(TestsPacketInstalmentStart)
test_packet_instalment_start_plus = unittest.TestLoader().loadTestsFromTestCase(TestsPacketInstalmentStartPlus)
test_packet_simple_premium_500 = unittest.TestLoader().loadTestsFromTestCase(TestsPacketSimplePremium5000)
test_registration = unittest.TestLoader().loadTestsFromTestCase(TestRegistration)
test_transfer_of_money = unittest.TestLoader().loadTestsFromTestCase(TestTransferOfMoney)
test_verification = unittest.TestLoader().loadTestsFromTestCase(TestVerification)
test_withdrawal_request = unittest.TestLoader().loadTestsFromTestCase(TestWithdrawalRequest) #включены доп.проверки на гугл аутентификацию
test_cashin_ttswift = unittest.TestLoader().loadTestsFromTestCase(TestCashInTtswift) #давно выключено на бою


extended_tests = unittest.TestSuite([test_auth,
                                       tests_cashin_advcash,
                                       test_cashin_ameria,
                                       test_cashin_bitcoin,
                                       tests_cashin_cryptonator,
                                       test_cashin_fasapay,
                                       tests_cashin_impex,
                                       tests_cashin_mera,
                                       test_cashin_pm,
                                       test_cashin_webmoney,
                                       test_packet_instalment_500,
                                       test_packet_instalment_start,
                                       test_packet_instalment_start_plus,
                                       test_packet_simple_premium_500,
                                       test_registration,
                                       test_transfer_of_money,
                                       test_verification])

check_packets = unittest.TestSuite([test_packet_instalment_500,
                                    test_packet_instalment_start,
                                    test_packet_instalment_start_plus,
                                    test_packet_simple_premium_500])

#basic_tests = unittest.TestSuite([tests_cashin_advcash])

basic_tests = unittest.TestSuite()
basic_tests.addTest(TestAuth('test_auth'))
basic_tests.addTest(TestCashInAdvcash('test_cashin_advcash_exmo'))
basic_tests.addTest(TestCashInAmeria('test_cashin_ameria_swift'))
basic_tests.addTest(TestCashInBitcoin('test_cashin_bitcoin'))
basic_tests.addTest(TestCashInCryptonator('test_cashin_cryptonator'))
basic_tests.addTest(TestCashInFasapay('test_cashin_fasapay'))
basic_tests.addTest(TestCashInImpex('test_cashin_impex_mastercard'))
basic_tests.addTest(TestCashInImpex('test_cashin_impex_visa'))
basic_tests.addTest(TestCashInImpex('test_cashin_impex_orange'))
basic_tests.addTest(TestCashInImpex('test_cashin_impex_payboutique'))
# basic_tests.addTest(TestCashInMegapolis('test_cashin_megapolis'))
# basic_tests.addTest(TestCashInMegapolisAgree('test_cashin_megapolis_agree'))
basic_tests.addTest(TestCashInMera('test_cashin_mera'))
basic_tests.addTest(TestCashInPm('test_cashin_pm'))
# basic_tests.addTest(TestCashInTinkoff('test_cashin_tinkoff'))
# basic_tests.addTest(TestCashInTinkoffAgree('test_cashin_tinkoff_agree'))
basic_tests.addTest(TestCashInWebmoney('test_cashin_webmoney'))
basic_tests.addTest(TestsPacketInstalment500('test_packet_instalment_500_through_account_a'))
basic_tests.addTest(TestsPacketInstalmentStart('test_packet_instalment_start_through_account_ab'))
basic_tests.addTest(TestsPacketInstalmentStartPlus('test_packet_instalment_start_plus_through_account_b'))
basic_tests.addTest(TestsPacketSimplePremium5000('test_packet_simple_premium_5000_through_account_c'))
basic_tests.addTest(TestRegistration('test_registration'))
basic_tests.addTest(TestTransferOfMoney('test_transfer_of_money'))
basic_tests.addTest(TestVerification('test_verification'))


test_tests = unittest.TestSuite()
test_tests.addTest(TestVerification('test_verification'))




# run the suite
#unittest.TextTestRunner(verbosity=2).run(test_testing)

dir = os.getcwd()
# open the report file
branch = "master"
report_title = "Results of a personal cabinet test."
if len(branch) > 2:
    report_title += " Branch: " + branch


# configure HTMLTestRunner options
runner= HTMLTestRunner.HTMLTestRunner(verbosity=2, title=report_title, test_name=branch)
#renner_oldani = HtmlTestRunner.HTMLTestRunner(report_title)


# run the suite using HTMLTestRunner
runner.run(basic_tests)






