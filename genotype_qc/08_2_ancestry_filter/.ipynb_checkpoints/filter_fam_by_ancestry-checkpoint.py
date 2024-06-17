# Define the ancestry file path and the FAM file path
ancestry_file_path = '/hg19/2_merge/ukb_hap_v2.lifted_already_GRCh37.GH.pruned.intersect1KG.5.Q.IDs'
fam_file_path = '/genotype_qc/06_hetero/geno_filter_6.3.fam'
filtered_out_ids_path='filter_out_ancestry_99%.txt'
threshold=0.95
ancestry_data = {}
with open(ancestry_file_path, 'r') as f:
    for line in f:
        parts = line.strip().split()
        patient_id = parts[0].split('_')[0]  # Assuming the ID is the first part before an underscore
        eur_ancestry = float(parts[1])  # EUR ancestry is in the second column
        ancestry_data[patient_id] = eur_ancestry

# Filter IDs based on EUR ancestry > threshold
filtered_ids = {k for k, v in ancestry_data.items() if v > threshold}

print("Patients meeting ancestry criteria:", len(filtered_ids))

# Initialize a list for IDs of patients who do not meet the criteria
filtered_out_ids = []

# Now, filter the FAM file
filtered_fam_lines = []
with open(fam_file_path, 'r') as fam_file:
    for line in fam_file:
        fam_id = line.strip().split()[0]
        if fam_id in filtered_ids:
            filtered_fam_lines.append(line)
        else:
            filtered_out_ids.append(fam_id)

# Write the filtered lines to a new FAM file
filtered_fam_file_path = 'filter_fam_by_ancestry_95%.fam'
with open(filtered_fam_file_path, 'w') as filtered_fam_file:
    filtered_fam_file.writelines(filtered_fam_lines)

# Write the IDs of filtered out patients to a separate file
with open(filtered_out_ids_path, 'w') as out_file:
    for id in filtered_out_ids:
        out_file.write(id + '\n')

# Output the number of filtered out patients
print("Patients filtered out:", len(filtered_out_ids))
