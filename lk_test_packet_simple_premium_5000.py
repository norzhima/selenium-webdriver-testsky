# -*- coding: utf-8 -*-
import lk_conf
from lk_class_pay_packets import PayPackets


class TestsPacketSimplePremium5000(PayPackets):
    #Варианты методов оплаты: pay_account_a, pay_account_b, pay_account_c, pay_account_ab, pay_account_ac, pay_account_bc,
    #pay_account_abc и сделаем внешние пс

    def test_packet_simple_premium_5000_through_account_c(self):
        self.check_packet(lk_conf.packet_premium_5000, lk_conf.pay_account_c)


