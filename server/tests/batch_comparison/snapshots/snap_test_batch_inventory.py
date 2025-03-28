# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots[
    "test_batch_inventory_ess_cvr_upload 1"
] = """Batch Name,Number of Ballots\r
BATCH1,6\r
BATCH2,8\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload 2"
] = """Batch Name,Choice 1-1,Choice 1-2,Write-In\r
BATCH1,2,2,0\r
BATCH2,4,4,0\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload 3"
] = """Batch Name,Number of Ballots\r
BATCH1,6\r
BATCH2,8\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload 4"
] = """Batch Name,Choice 1-1,Choice 1-2,Write-In\r
BATCH1,2,2,0\r
BATCH2,4,4,0\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload 5"
] = """Batch Name,Number of Ballots\r
BATCH1,6\r
BATCH2,8\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload 6"
] = """Batch Name,Choice 1-1,Choice 1-2,Write-In\r
BATCH1,2,2,0\r
BATCH2,4,4,0\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload 7"
] = """Batch Name,Number of Ballots\r
BATCH1,6\r
BATCH2,8\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload 8"
] = """Batch Name,Choice 1-1,Choice 1-2,Write-In\r
BATCH1,2,2,0\r
BATCH2,4,4,0\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload_multi_contest 1"
] = """Batch Name,Number of Ballots\r
BATCH1,6\r
BATCH2,8\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload_multi_contest 2"
] = """Batch Name,Contest 1 - Choice 1-1,Contest 1 - Choice 1-2,Contest 1 - Write-In,Contest 2 - Choice 2-1,Contest 2 - Choice 2-2,Contest 2 - Choice 2-3,Contest 2 - Write-In\r
BATCH1,2,2,0,6,0,0,0\r
BATCH2,4,4,0,2,4,2,0\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload_no_ballot_file 1"
] = """Batch Name,Number of Ballots\r
Batch 1,4\r
Batch 2,5\r
Batch 3,5\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload_no_ballot_file 2"
] = """Batch Name,Choice 1-1,Choice 1-2,Write-In\r
Batch 1,2,1,1\r
Batch 2,1,2,0\r
Batch 3,2,2,1\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload_no_ballot_file 3"
] = """Batch Name,Number of Ballots\r
Batch 1,4\r
Batch 2,5\r
Batch 3,5\r
"""

snapshots[
    "test_batch_inventory_ess_cvr_upload_no_ballot_file 4"
] = """Batch Name,Choice 1-1,Choice 1-2,Write-In\r
Batch 1,2,1,1\r
Batch 2,1,2,0\r
Batch 3,2,2,1\r
"""

snapshots[
    "test_batch_inventory_excel_tabulator_status_file 1"
] = """Batch Inventory Worksheet\r
\r
Section 1: Check Ballot Groups\r
1. Compare the CVR Ballot Count for each ballot group to your voter check-in data.\r
2. Ensure that the numbers reconcile. If there is a large discrepancy contact your SOS liaison.\r
\r
Ballot Group,CVR Ballot Count,Checked? (Type Yes/No)\r
Election Day,13,\r
Mail,2,\r
\r
Section 2: Check Batches\r
1. Locate each batch in storage.\r
2. Confirm the CVR Ballot Count is correct using associated documentation. Do NOT count the ballots. If there is a large discrepancy contact your SOS liaison.\r
3. Make sure there are no batches missing from this worksheet.\r
\r
Batch,CVR Ballot Count,Checked? (Type Yes/No)\r
Tabulator 1 - BATCH1,3,\r
Tabulator 1 - BATCH2,3,\r
Tabulator 2 - BATCH1,3,\r
Tabulator 2 - BATCH2,6,\r
"""

snapshots[
    "test_batch_inventory_happy_path 1"
] = """Batch Inventory Worksheet\r
\r
Section 1: Check Ballot Groups\r
1. Compare the CVR Ballot Count for each ballot group to your voter check-in data.\r
2. Ensure that the numbers reconcile. If there is a large discrepancy contact your SOS liaison.\r
\r
Ballot Group,CVR Ballot Count,Checked? (Type Yes/No)\r
Election Day,13,\r
Mail,2,\r
\r
Section 2: Check Batches\r
1. Locate each batch in storage.\r
2. Confirm the CVR Ballot Count is correct using associated documentation. Do NOT count the ballots. If there is a large discrepancy contact your SOS liaison.\r
3. Make sure there are no batches missing from this worksheet.\r
\r
Batch,CVR Ballot Count,Checked? (Type Yes/No)\r
Tabulator 1 - BATCH1,3,\r
Tabulator 1 - BATCH2,3,\r
Tabulator 2 - BATCH1,3,\r
Tabulator 2 - BATCH2,6,\r
"""

snapshots[
    "test_batch_inventory_happy_path 2"
] = """Container,Batch Name,Number of Ballots\r
Election Day,Tabulator 1 - BATCH1,3\r
Election Day,Tabulator 1 - BATCH2,3\r
Mail,Tabulator 2 - BATCH1,3\r
Election Day,Tabulator 2 - BATCH2,6\r
"""

snapshots[
    "test_batch_inventory_happy_path 3"
] = """Batch Name,Choice 1-1,Choice 1-2,Write-In\r
Tabulator 1 - BATCH1,1,1,1\r
Tabulator 1 - BATCH2,2,1,0\r
Tabulator 2 - BATCH1,2,1,0\r
Tabulator 2 - BATCH2,2,0,0\r
"""

snapshots[
    "test_batch_inventory_happy_path_cvrs_with_extra_spaces 1"
] = """Batch Inventory Worksheet\r
\r
Section 1: Check Ballot Groups\r
1. Compare the CVR Ballot Count for each ballot group to your voter check-in data.\r
2. Ensure that the numbers reconcile. If there is a large discrepancy contact your SOS liaison.\r
\r
Ballot Group,CVR Ballot Count,Checked? (Type Yes/No)\r
Election Day,13,\r
Mail,2,\r
\r
Section 2: Check Batches\r
1. Locate each batch in storage.\r
2. Confirm the CVR Ballot Count is correct using associated documentation. Do NOT count the ballots. If there is a large discrepancy contact your SOS liaison.\r
3. Make sure there are no batches missing from this worksheet.\r
\r
Batch,CVR Ballot Count,Checked? (Type Yes/No)\r
Tabulator 1 - BATCH1,3,\r
Tabulator 1 - BATCH2,3,\r
Tabulator 2 - BATCH1,3,\r
Tabulator 2 - BATCH2,6,\r
"""

snapshots[
    "test_batch_inventory_happy_path_cvrs_with_extra_spaces 2"
] = """Container,Batch Name,Number of Ballots\r
Election Day,Tabulator 1 - BATCH1,3\r
Election Day,Tabulator 1 - BATCH2,3\r
Mail,Tabulator 2 - BATCH1,3\r
Election Day,Tabulator 2 - BATCH2,6\r
"""

snapshots[
    "test_batch_inventory_happy_path_cvrs_with_extra_spaces 3"
] = """Batch Name,Choice 1-1,Choice 1-2,Write-In\r
Tabulator 1 - BATCH1,1,1,1\r
Tabulator 1 - BATCH2,2,1,0\r
Tabulator 2 - BATCH1,2,1,0\r
Tabulator 2 - BATCH2,2,0,0\r
"""

snapshots[
    "test_batch_inventory_happy_path_cvrs_with_leading_equal_signs 1"
] = """Batch Inventory Worksheet\r
\r
Section 1: Check Ballot Groups\r
1. Compare the CVR Ballot Count for each ballot group to your voter check-in data.\r
2. Ensure that the numbers reconcile. If there is a large discrepancy contact your SOS liaison.\r
\r
Ballot Group,CVR Ballot Count,Checked? (Type Yes/No)\r
Election Day,13,\r
Mail,2,\r
\r
Section 2: Check Batches\r
1. Locate each batch in storage.\r
2. Confirm the CVR Ballot Count is correct using associated documentation. Do NOT count the ballots. If there is a large discrepancy contact your SOS liaison.\r
3. Make sure there are no batches missing from this worksheet.\r
\r
Batch,CVR Ballot Count,Checked? (Type Yes/No)\r
Tabulator 1 - BATCH1,3,\r
Tabulator 1 - BATCH2,3,\r
Tabulator 2 - BATCH1,3,\r
Tabulator 2 - BATCH2,6,\r
"""

snapshots[
    "test_batch_inventory_happy_path_cvrs_with_leading_equal_signs 2"
] = """Container,Batch Name,Number of Ballots\r
Election Day,Tabulator 1 - BATCH1,3\r
Election Day,Tabulator 1 - BATCH2,3\r
Mail,Tabulator 2 - BATCH1,3\r
Election Day,Tabulator 2 - BATCH2,6\r
"""

snapshots[
    "test_batch_inventory_happy_path_cvrs_with_leading_equal_signs 3"
] = """Batch Name,Choice 1-1,Choice 1-2,Write-In\r
Tabulator 1 - BATCH1,1,1,1\r
Tabulator 1 - BATCH2,2,1,0\r
Tabulator 2 - BATCH1,2,1,0\r
Tabulator 2 - BATCH2,2,0,0\r
"""

snapshots[
    "test_batch_inventory_happy_path_multi_contest_batch_comparison 1"
] = """Batch Inventory Worksheet\r
\r
Section 1: Check Ballot Groups\r
1. Compare the CVR Ballot Count for each ballot group to your voter check-in data.\r
2. Ensure that the numbers reconcile. If there is a large discrepancy contact your SOS liaison.\r
\r
Ballot Group,CVR Ballot Count,Checked? (Type Yes/No)\r
Election Day,13,\r
Mail,2,\r
\r
Section 2: Check Batches\r
1. Locate each batch in storage.\r
2. Confirm the CVR Ballot Count is correct using associated documentation. Do NOT count the ballots. If there is a large discrepancy contact your SOS liaison.\r
3. Make sure there are no batches missing from this worksheet.\r
\r
Batch,CVR Ballot Count,Checked? (Type Yes/No)\r
Tabulator 1 - BATCH1,3,\r
Tabulator 1 - BATCH2,3,\r
Tabulator 2 - BATCH1,3,\r
Tabulator 2 - BATCH2,6,\r
"""

snapshots[
    "test_batch_inventory_happy_path_multi_contest_batch_comparison 2"
] = """Container,Batch Name,Number of Ballots\r
Election Day,Tabulator 1 - BATCH1,3\r
Election Day,Tabulator 1 - BATCH2,3\r
Mail,Tabulator 2 - BATCH1,3\r
Election Day,Tabulator 2 - BATCH2,6\r
"""

snapshots[
    "test_batch_inventory_happy_path_multi_contest_batch_comparison 3"
] = """Batch Name,Contest 1 - Choice 1-1,Contest 1 - Choice 1-2,Contest 1 - Write-In,Contest 2 - Choice 2-1,Contest 2 - Choice 2-2,Contest 2 - Choice 2-3,Contest 2 - Write-In\r
Tabulator 1 - BATCH1,1,1,1,3,2,1,0\r
Tabulator 1 - BATCH2,2,1,0,3,1,2,0\r
Tabulator 2 - BATCH1,2,1,0,3,2,1,0\r
Tabulator 2 - BATCH2,2,0,0,6,2,4,0\r
"""

snapshots[
    "test_batch_inventory_hart_cvr_upload 1"
] = """Batch Name,Number of Ballots\r
BATCH1,4\r
BATCH2,3\r
BATCH3,2\r
BATCH4,2\r
"""

snapshots[
    "test_batch_inventory_hart_cvr_upload 2"
] = """Batch Name,Choice 1-1,Choice 1-2,Write-In\r
BATCH1,1,2,0\r
BATCH2,2,1,0\r
BATCH4,1,0,1\r
BATCH3,0,0,0\r
"""

snapshots[
    "test_batch_inventory_hart_cvr_upload_multi_contest 1"
] = """Batch Name,Number of Ballots\r
BATCH1,3\r
BATCH2,3\r
BATCH3,2\r
BATCH4,2\r
"""

snapshots[
    "test_batch_inventory_hart_cvr_upload_multi_contest 2"
] = """Batch Name,Contest 1 - Choice 1-1,Contest 1 - Choice 1-2,Contest 1 - Write-In,Contest 2 - Choice 2-1,Contest 2 - Choice 2-2,Contest 2 - Choice 2-3,Contest 2 - Write-In\r
BATCH1,1,2,0,3,2,1,0\r
BATCH2,2,1,0,3,1,2,0\r
BATCH3,0,0,0,0,1,1,0\r
BATCH4,1,0,1,0,0,1,1\r
"""
