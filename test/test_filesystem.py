"""Tests for filesystem.py"""

from os import path
from typing import List

import ctakes_examples


def test_curated_examples():
    # Update count when you add new ones!
    check_examples(ctakes_examples.list_curated(), 2363)


def test_synthetic_examples():
    # Update count when you add new ones!
    check_examples(ctakes_examples.list_synthetic(), 20)


def test_read_curated():
    assert ctakes_examples.read_curated('mri-ankle-2') == """

EXAM: MRI OF THE RIGHT ANKLE

CLINICAL: Pain.

FINDINGS:  
The bone marrow demonstrates normal signal intensity. There is no evidence of
bone contusion or fracture. There is no evidence of joint effusion. Tendinous
structures surrounding the ankle joint are intact. No abnormal mass or fluid
collection is seen surrounding the ankle joint.

IMPRESSION : NORMAL MRI OF THE RIGHT ANKLE."""


def test_read_synthetic():
    assert ctakes_examples.read_synthetic('c3493c19-0483-d3ba-6822-bff4bf7c5c23') == """
2021-05-14

# Chief Complaint
No complaints.

# History of Present Illness
Monty345
 is a 11 year-old non-hispanic white male. Patient has a history of muscle pain (finding), covid-19, fever (finding), sputum finding (finding), headache (finding), joint pain (finding), cough (finding), suspected covid-19.

# Social History
 Patient has never smoked.


Patient comes from a middle socioeconomic background.

Patient currently has UnitedHealthcare.

# Allergies
No Known Allergies.

# Medications
No Active Medications.

# Assessment and Plan
Patient is presenting with viral sinusitis (disorder). 

## Plan




2020-11-19

# Chief Complaint
No complaints.

# History of Present Illness
Monty345
 is a 11 year-old non-hispanic white male. Patient has a history of muscle pain (finding), covid-19, fever (finding), sputum finding (finding), headache (finding), joint pain (finding), cough (finding), suspected covid-19.

# Social History
 Patient has never smoked.


Patient comes from a middle socioeconomic background.

Patient currently has Blue Cross Blue Shield.

# Allergies
No Known Allergies.

# Medications
No Active Medications.

# Assessment and Plan


## Plan
Patient was given the following immunizations: tdap, influenza, seasonal, injectable, preservative free, hpv, quadrivalent, meningococcal mcv4p. 



2020-02-29

# Chief Complaint
No complaints.

# History of Present Illness
Monty345
 is a 10 year-old non-hispanic white male.

# Social History
 Patient has never smoked.


Patient comes from a middle socioeconomic background.

Patient currently has Blue Cross Blue Shield.

# Allergies
No Known Allergies.

# Medications
No Active Medications.

# Assessment and Plan
Patient is presenting with headache (finding), cough (finding), sputum finding (finding), muscle pain (finding), joint pain (finding), fever (finding), suspected covid-19, covid-19. 

## Plan

The following procedures were conducted:
- face mask (physical object)
The patient was placed on a careplan:
- infectious disease care plan (record artifact)
- infectious disease care plan (record artifact)



2019-11-14

# Chief Complaint
No complaints.

# History of Present Illness
Monty345
 is a 10 year-old non-hispanic white male.

# Social History
 Patient has never smoked.


Patient comes from a middle socioeconomic background.

Patient currently has Blue Cross Blue Shield.

# Allergies
No Known Allergies.

# Medications
No Active Medications.

# Assessment and Plan


## Plan
Patient was given the following immunizations: influenza, seasonal, injectable, preservative free. 
The following procedures were conducted:
- medication reconciliation (procedure)



"""


###############################################################################
#
# Helpers
#
###############################################################################

def check_examples(examples: List[str], expected_count: int) -> None:
    # Test that we return all examples
    assert expected_count == len(examples)

    # Test that it's sorted
    assert sorted(examples) == examples

    # Test that the returned paths are absolute paths and readable
    assert path.isabs(examples[0])
    with open(examples[0], 'r', encoding='utf8') as f:
        assert len(f.read()) > 0
