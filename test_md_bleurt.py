from bleurt import score
from bleurt import score_vector

checkpoint_path = "finetuned_models/multihead_mixed_complete_paraphrase_vector_score/export/bleurt_best_all_heads/1778197869"
scorer = score_vector.BleurtScorer(checkpoint_path)

references_test = ["This is a great day today."]
candidates_test = ["This is a bad day today."]
scores = scorer.score(references=references_test, candidates=candidates_test)
print("Similar sentence score", scores)
print()

# "text": "A paracentesis was performed on her abdomen. A total of 5 liters of ascitic fluid were removed. The fluid analysis is pending."}
# "text": "The patient's fasting blood glucose was 155 mg/dL. This meets the criteria for a diagnosis of diabetes mellitus."}
# "text": "The patient's condition is stable. He will be transferred from the step-down unit to the medical floor today."}
# "text": "If the patient's headache worsens, he should proceed to the emergency department. He was given a prescription for Rizatriptan. He has a history of migraines."}
# "text": "The father's blood pressure is 118/76 mmHg. His hypertension is well-controlled."}


references = ["A paracentesis was performed on her abdomen. A total of 4 liters of ascitic fluid were removed. The fluid analysis is pending."]
paraphrase = ["An abdominal paracentesis was performed on her. A total of 4 liters of ascitic fluid were removed. The fluid analysis is pending."]
negative = ["A paracentesis was performed on her abdomen. A total of 5 liters of ascitic fluid were removed. The fluid analysis is pending."]
print("Anchor Text: ", references[0])
print("Positive Text: ", paraphrase[0])
print("Negative Text: ", negative[0])
scores_pos = scorer.score(references=references, candidates=paraphrase)
scores_neg = scorer.score(references=references, candidates=negative)
print("Positive score", scores_pos)
print("Negative score", scores_neg)
print()



references = ["The patient's fasting blood glucose was 130 mg/dL. This meets the criteria for a diagnosis of diabetes mellitus."]
paraphrase = ["The patient's fasting blood sugar was recorded at 130 mg/dL. This meets the criteria for a diagnosis of diabetes mellitus."]
negative = ["The patient's fasting blood glucose was 155 mg/dL. This meets the criteria for a diagnosis of diabetes mellitus."]
print("Anchor Text: ", references[0])
print("Positive Text: ", paraphrase[0])
print("Negative Text: ", negative[0])
scores_pos = scorer.score(references=references, candidates=paraphrase)
scores_neg = scorer.score(references=references, candidates=negative)
print("Positive score", scores_pos)
print("Negative score", scores_neg)
print()

references = ["The patient's condition is stable. He will be transferred from the ICU to the medical floor today."]
paraphrase = ["The patient is in a stable condition. He will be transferred from the ICU to the medical floor today."]
negative = ["The patient's condition is stable. He will be transferred from the step-down unit to the medical floor today."]
print("Anchor Text: ", references[0])
print("Positive Text: ", paraphrase[0])
print("Negative Text: ", negative[0])
scores_pos = scorer.score(references=references, candidates=paraphrase)
scores_neg = scorer.score(references=references, candidates=negative)
print("Positive score", scores_pos)
print("Negative score", scores_neg)
print()


references = ["If the patient's headache worsens, he should proceed to the emergency department. He was given a prescription for Sumatriptan. He has a history of migraines."]
paraphrase = ["Should the patient's headache worsen, he should proceed to the emergency department. He was given a prescription for Sumatriptan. He has a history of migraines."]
negative = ["If the patient's headache worsens, he should proceed to the emergency department. He was given a prescription for Rizatriptan. He has a history of migraines."]
print("Anchor Text: ", references[0])
print("Positive Text: ", paraphrase[0])
print("Negative Text: ", negative[0])
scores_pos = scorer.score(references=references, candidates=paraphrase)
scores_neg = scorer.score(references=references, candidates=negative)
print("Positive score", scores_pos)
print("Negative score", scores_neg)
print()


references = ["The patient's blood pressure is 118/76 mmHg. His hypertension is well-controlled."]
paraphrase = ["The patient has a blood pressure of 118/76 mmHg. His hypertension is well-controlled."]
negative = ["The father's blood pressure is 118/76 mmHg. His hypertension is well-controlled."]
print("Anchor Text: ", references[0])
print("Positive Text: ", paraphrase[0])
print("Negative Text: ", negative[0])
scores_pos = scorer.score(references=references, candidates=paraphrase)
scores_neg = scorer.score(references=references, candidates=negative)
print("Positive score", scores_pos)
print("Negative score", scores_neg)
print()
