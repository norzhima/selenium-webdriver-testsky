# -*- coding: utf-8 -*-
import lk_conf
from lk_class_pay_packets import PayPackets


class TestsPacketInstalmentStartPlus(PayPackets):
    #Варианты методов оплаты: pay_account_a, pay_account_b, pay_account_c, pay_account_ab, pay_account_ac, pay_account_bc,
    #pay_account_abc и сделаем внешние пс

    #@unittest.skip("Тестирование пакета instalment_start_plus временно выключено.")
    def test_packet_instalment_start_plus_through_account_b(self):
        self.check_packet(lk_conf.packet_start_plus, lk_conf.pay_account_b)
