# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots[
    "test_not_found_ballots 1"
] = """######## ELECTION INFO ########\r
Organization,Election Name,State\r
Test Org test_not_found_ballots,Test Election,CA\r
\r
######## CONTESTS ########\r
Contest Name,Targeted?,Number of Winners,Votes Allowed,Total Ballots Cast,Vote Totals\r
Contest 1,Targeted,1,1,1000,candidate 1: 600; candidate 2: 400\r
Contest 2,Opportunistic,2,2,600,candidate 1: 200; candidate 2: 300; candidate 3: 100\r
\r
######## AUDIT SETTINGS ########\r
Audit Name,Audit Type,Audit Math Type,Risk Limit,Random Seed,Online Data Entry?\r
Test Audit test_not_found_ballots,BALLOT_POLLING,BRAVO,10%,1234567890,Yes\r
\r
######## AUDIT BOARDS ########\r
Jurisdiction Name,Audit Board Name,Member 1 Name,Member 1 Affiliation,Member 2 Name,Member 2 Affiliation\r
J1,Audit Board #1,,,,\r
J1,Audit Board #2,,,,\r
\r
######## ROUNDS ########\r
Round Number,Contest Name,Targeted?,Sample Size,Risk Limit Met?,P-Value,Start Time,End Time,Audited Votes\r
1,Contest 1,Targeted,119,Yes,0.0000000044,DATETIME,DATETIME,candidate 1: 119; candidate 2: 0; Ballots not found (counted for loser): 11\r
1,Contest 2,Opportunistic,,Yes,0.0000043592,DATETIME,DATETIME,candidate 1: 57; candidate 2: 55; candidate 3: 0; Ballots not found (counted for loser): 10\r
\r
######## SAMPLED BALLOTS ########\r
Jurisdiction Name,Batch Name,Ballot Position,Ticket Numbers: Contest 1,Audited?,Audit Result: Contest 1,Audit Result: Contest 2\r
J1,1,3,Round 1: 0.088404500051420169,AUDITED,candidate 1,candidate 2\r
J1,1,4,Round 1: 0.056455363529765325,AUDITED,candidate 1,candidate 2\r
J1,1,6,Round 1: 0.063938772948313277,AUDITED,candidate 1,candidate 1\r
J1,1,23,Round 1: 0.026709936196363079,AUDITED,candidate 1,candidate 1\r
J1,2,2,Round 1: 0.091912034655946169,AUDITED,candidate 1,candidate 2\r
J1,2,6,Round 1: 0.028662515227396225,AUDITED,candidate 1,candidate 1\r
J1,2,25,Round 1: 0.023369462249873393,AUDITED,candidate 1,candidate 2\r
J1,2,29,Round 1: 0.071025445549972134,AUDITED,candidate 1,candidate 2\r
J1,2,30,Round 1: 0.028807763145463000,AUDITED,candidate 1,candidate 2\r
J1,2,39,Round 1: 0.115805768632379354,AUDITED,candidate 1,candidate 1\r
J1,2,70,Round 1: 0.032079033020155699,AUDITED,candidate 1,candidate 2\r
J1,2,73,Round 1: 0.108526924051470744,AUDITED,candidate 1,candidate 2\r
J1,2,75,Round 1: 0.035640239666365080,AUDITED,candidate 1,candidate 2\r
J1,2,77,Round 1: 0.061243853397465359,AUDITED,candidate 1,candidate 2\r
J1,2,84,Round 1: 0.095975333017344763,AUDITED,candidate 1,candidate 1\r
J1,2,88,Round 1: 0.071804966402309250,AUDITED,candidate 1,candidate 1\r
J1,2,89,Round 1: 0.054646592241035729,AUDITED,candidate 1,candidate 1\r
J1,2,100,Round 1: 0.101396216379465808,AUDITED,candidate 1,candidate 1\r
J1,3,2,Round 1: 0.096258425102788892,AUDITED,candidate 1,candidate 1\r
J1,3,11,Round 1: 0.093515621534103985,AUDITED,candidate 1,candidate 2\r
J1,3,38,Round 1: 0.018230756390081779,AUDITED,candidate 1,candidate 2\r
J1,3,40,Round 1: 0.014739823561707141,AUDITED,candidate 1,candidate 2\r
J1,3,50,Round 1: 0.001315804865633048,NOT_FOUND,candidate 1,candidate 2\r
J1,3,82,Round 1: 0.046244912686705392,AUDITED,candidate 1,candidate 2\r
J1,3,84,Round 1: 0.101133216050746816,AUDITED,candidate 1,candidate 1\r
J1,3,97,Round 1: 0.000454186428506763,NOT_FOUND,candidate 1,candidate 1\r
J1,3,100,"Round 1: 0.000619826143680938, 0.118040423696597067",NOT_FOUND,candidate 1,candidate 1\r
J1,3,106,Round 1: 0.061350998660180108,AUDITED,candidate 1,candidate 1\r
J1,3,117,Round 1: 0.026152774099611906,AUDITED,candidate 1,candidate 2\r
J1,3,121,Round 1: 0.068048811291378543,AUDITED,candidate 1,candidate 1\r
J1,4,3,Round 1: 0.010306372247476217,NOT_FOUND,candidate 1,candidate 1\r
J1,4,5,"Round 1: 0.080704071573746128, 0.099341639942774926",AUDITED,candidate 1,candidate 1\r
J1,4,6,Round 1: 0.104029943609805403,AUDITED,candidate 1,candidate 1\r
J1,4,7,Round 1: 0.042092437205341423,AUDITED,candidate 1,candidate 1\r
J1,4,26,Round 1: 0.074248137323249137,AUDITED,candidate 1,candidate 2\r
J1,4,44,Round 1: 0.042228065622768503,AUDITED,candidate 1,candidate 2\r
J1,4,61,Round 1: 0.054099586219482054,AUDITED,candidate 1,candidate 2\r
J1,4,63,Round 1: 0.003836186945975918,NOT_FOUND,candidate 1,candidate 1\r
J1,4,66,Round 1: 0.096975818551066342,AUDITED,candidate 1,candidate 2\r
J1,4,67,Round 1: 0.091470963043987134,AUDITED,candidate 1,candidate 1\r
J1,4,90,Round 1: 0.032834360453541187,AUDITED,candidate 1,candidate 2\r
J1,4,94,Round 1: 0.111941491629163402,AUDITED,candidate 1,candidate 2\r
J1,4,105,Round 1: 0.023112222444256629,AUDITED,candidate 1,candidate 1\r
J1,4,117,Round 1: 0.082550146523358971,AUDITED,candidate 1,candidate 2\r
J1,4,120,Round 1: 0.075775152592425405,AUDITED,candidate 1,candidate 1\r
J1,4,158,Round 1: 0.105230770286479126,AUDITED,candidate 1,candidate 1\r
J1,4,166,Round 1: 0.077882036529627073,AUDITED,candidate 1,candidate 2\r
J1,4,177,Round 1: 0.077933165074758787,AUDITED,candidate 1,candidate 1\r
J1,4,195,Round 1: 0.100521475517045244,AUDITED,candidate 1,candidate 2\r
J1,4,198,Round 1: 0.070349800984198330,AUDITED,candidate 1,candidate 1\r
J1,4,208,Round 1: 0.036612236698180247,AUDITED,candidate 1,candidate 1\r
J1,4,215,Round 1: 0.040595725718922402,AUDITED,candidate 1,candidate 1\r
J1,4,217,Round 1: 0.062330471179110521,AUDITED,candidate 1,candidate 2\r
J1,4,220,Round 1: 0.068494770695355835,AUDITED,candidate 1,candidate 2\r
J1,4,222,Round 1: 0.072280927514051282,AUDITED,candidate 1,candidate 2\r
J1,4,241,Round 1: 0.069869996497425336,AUDITED,candidate 1,candidate 2\r
J1,4,249,Round 1: 0.046501275943279774,AUDITED,candidate 1,candidate 1\r
J1,4,256,Round 1: 0.040546706799122951,AUDITED,candidate 1,candidate 2\r
J1,4,263,Round 1: 0.013595936546478868,NOT_FOUND,candidate 1,candidate 1\r
J1,4,273,Round 1: 0.029372995614232565,AUDITED,candidate 1,candidate 1\r
J1,4,280,Round 1: 0.117155998071883033,AUDITED,candidate 1,candidate 2\r
J1,4,290,Round 1: 0.000461433395583052,NOT_FOUND,candidate 1,candidate 2\r
J1,4,294,Round 1: 0.085416334659259955,AUDITED,candidate 1,candidate 2\r
J1,4,308,Round 1: 0.051954609019659065,AUDITED,candidate 1,candidate 1\r
J1,4,325,Round 1: 0.059827989431571177,AUDITED,candidate 1,candidate 2\r
J1,4,335,Round 1: 0.077728803876745538,AUDITED,candidate 1,candidate 1\r
J1,4,336,Round 1: 0.085191621074810971,AUDITED,candidate 1,candidate 1\r
J1,4,338,Round 1: 0.097544908368535753,AUDITED,candidate 1,candidate 1\r
J1,4,339,Round 1: 0.104640686198153541,AUDITED,candidate 1,candidate 2\r
J1,4,347,Round 1: 0.032225479026399263,AUDITED,candidate 1,candidate 1\r
J1,4,364,"Round 1: 0.014195240836456557, 0.067991977068525173",AUDITED,candidate 1,candidate 1\r
J1,4,375,"Round 1: 0.028954249616875816, 0.100423932182991905",AUDITED,candidate 1,candidate 2\r
J1,4,376,Round 1: 0.041784965549179532,AUDITED,candidate 1,candidate 2\r
J1,4,383,Round 1: 0.037428227356516192,AUDITED,candidate 1,candidate 2\r
J1,4,390,Round 1: 0.023508408392288091,AUDITED,candidate 1,candidate 1\r
J1,4,400,Round 1: 0.033664359681262958,AUDITED,candidate 1,candidate 1\r
J2,1,3,Round 1: 0.026974562209906179,AUDITED,candidate 1,candidate 2\r
J2,1,18,Round 1: 0.014104975821697965,NOT_FOUND,candidate 1,candidate 2\r
J2,2,4,Round 1: 0.044147335849878093,AUDITED,candidate 1,candidate 2\r
J2,2,6,Round 1: 0.011988982664080463,NOT_FOUND,candidate 1,candidate 2\r
J2,2,10,Round 1: 0.045351581516619860,AUDITED,candidate 1,candidate 1\r
J2,3,18,Round 1: 0.069668342793075274,AUDITED,candidate 1,candidate 1\r
J2,3,30,Round 1: 0.042672901163402832,AUDITED,candidate 1,candidate 1\r
J2,3,32,Round 1: 0.089615926764951869,AUDITED,candidate 1,candidate 1\r
J2,3,47,Round 1: 0.040062098731520309,AUDITED,candidate 1,candidate 1\r
J2,3,50,Round 1: 0.108342102764767955,AUDITED,candidate 1,candidate 1\r
J2,3,51,"Round 1: 0.096120553260524803, 0.113789621888339460",AUDITED,candidate 1,candidate 2\r
J2,3,56,"Round 1: 0.091048982285661053, 0.101378875314002018",AUDITED,candidate 1,candidate 2\r
J2,3,58,Round 1: 0.045253125083783178,AUDITED,candidate 1,candidate 1\r
J2,3,61,Round 1: 0.096604572871094987,AUDITED,candidate 1,candidate 1\r
J2,3,71,Round 1: 0.088124330140694101,AUDITED,candidate 1,candidate 1\r
J2,3,76,Round 1: 0.077988294597998248,AUDITED,candidate 1,candidate 2\r
J2,3,88,Round 1: 0.109322394754273640,AUDITED,candidate 1,candidate 1\r
J2,3,97,Round 1: 0.096444576053280526,AUDITED,candidate 1,candidate 2\r
J2,3,101,"Round 1: 0.014786076170605607, 0.033699457455768933",AUDITED,candidate 1,candidate 1\r
J2,3,106,Round 1: 0.045266995759010649,AUDITED,candidate 1,candidate 2\r
J2,3,110,Round 1: 0.072858131275512064,AUDITED,candidate 1,candidate 1\r
J2,3,122,Round 1: 0.073465505074563528,AUDITED,candidate 1,candidate 1\r
J2,3,125,Round 1: 0.115573400982398903,AUDITED,candidate 1,candidate 2\r
J2,3,154,Round 1: 0.010022804537356634,NOT_FOUND,candidate 1,candidate 2\r
J2,3,157,Round 1: 0.103642122132931710,AUDITED,candidate 1,candidate 2\r
J2,3,165,Round 1: 0.047889972941670238,AUDITED,candidate 1,candidate 2\r
J2,3,174,Round 1: 0.059804486813794551,AUDITED,candidate 1,candidate 1\r
J2,3,180,Round 1: 0.083278065379106609,AUDITED,candidate 1,candidate 2\r
J2,3,181,Round 1: 0.077209685743241616,AUDITED,candidate 1,candidate 2\r
J2,3,191,Round 1: 0.073322038933809532,AUDITED,candidate 1,candidate 2\r
J2,3,196,Round 1: 0.034526859969954916,AUDITED,candidate 1,candidate 1\r
J2,3,206,Round 1: 0.028858006840055629,AUDITED,candidate 1,candidate 1\r
J2,3,209,Round 1: 0.105574445837861061,AUDITED,candidate 1,candidate 2\r
J2,3,214,Round 1: 0.082699452005387947,AUDITED,candidate 1,candidate 1\r
J2,4,34,Round 1: 0.060816634473886193,AUDITED,candidate 1,candidate 1\r
J2,4,37,Round 1: 0.092786549356518562,AUDITED,candidate 1,candidate 1\r
"""
