# -*- coding: utf-8 -*-
import lk_conf
from lk_class_pay_packets import PayPackets


class TestsPacketInstalmentStart(PayPackets):
    #Варианты методов оплаты: pay_account_a, pay_account_b, pay_account_c, pay_account_ab, pay_account_ac, pay_account_bc,
    #pay_account_abc и сделаем внешние пс

    #@unittest.skip("Тестирование пакета instalment_start disabled.")
    def test_packet_instalment_start_through_account_ab(self):
        self.check_packet(lk_conf.packet_start, lk_conf.pay_account_ab)