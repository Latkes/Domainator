#!/usr/bin/env python3
import logging

from src.domainator import Domainator
from src.utils import *

logging.basicConfig(filename='log.log', filemode='w', level=logging.DEBUG)


def passive_menu(sb: Domainator):
    while 1:
        cc = choose(['Whois Lookup', 'Reverse IP Lookup'])
        if cc < 0:
            break
        elif cc == 0:
            sb.whois()
        elif cc == 1:
            sb.banners_cloud_flare()
        elif cc == 2:
            while 1:
                ccc = choose(['HackerTarget', 'YouGetSignal'], 'Choose method:')
                if ccc < 0:
                    break
                elif ccc == 0:
                    sb.reverse_HT()
                elif ccc == 1:
                    sb.reverse_YGS()


def active_menu(sb: Domainator):
    while 1:
        cc = choose(
            ['Grab Headers & CloudFlare', 'Site Speed Check',
             'Sub-domains Scan', 'Crawler'])
        if cc < 0:
            break
        if cc == 0:
            sb.banners_cloud_flare()
        elif cc == 1:
            sb.speed_check()
        elif cc == 2:
            sb.find_subdomains()
        elif cc == 3:
            sb.crawler.menu()


def main_menu(sb: Domainator):
    while 1:
        c = choose(['Passive', 'Active'])
        if c < 0:
            break
        if c == 0:
            passive_menu(sb)
        if c == 1:
            active_menu(sb)


if __name__ == '__main__':
    logging.info('Starting')
    try:
        main_menu(Domainator())
    except KeyboardInterrupt:
        pr('Interrupted!', '!')
