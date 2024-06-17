import pandas as pd
def add_visit_info(negative_features,positive_features,visit_number):
    """
    add visit info to the head of feature to match correct column in the df
    """
    negative_features_updated = []
    positive_features_updated = []
    if visit_number!="EHR":
        if len(negative_features)!=0:
            for feature in negative_features:
                new_feature = "instance_"+str(visit_number)+".INTVW_"+feature
                negative_features_updated.append(new_feature)
        if len(positive_features)!=0:
            for feature in positive_features:
                new_feature = "instance_"+str(visit_number)+".INTVW_"+feature
                positive_features_updated.append(new_feature)
    elif visit_number=="EHR":
        if len(negative_features)!=0:
            for feature in negative_features:
                new_feature = visit_number+"_"+feature
                negative_features_updated.append(new_feature)
        if len(positive_features)!=0:
            for feature in positive_features:
                new_feature = visit_number+"_"+feature
                positive_features_updated.append(new_feature)
    else:
        raise ValueError("Incorrect input: input_value must be 0 or 1 or 2 or EHR")
    return negative_features_updated,positive_features_updated
def filtering_HF(df,recruit_df,negative_feature:list,positive_feature:list,visit_number)->pd.DataFrame:
    """
    This function tries to filter according to negative and positive features.
    If any negative features are not nan, then, check positive features. If non positive
    features existed, then it is prevalent case
    """
    negative_feature,positive_feature = add_visit_info(negative_feature,positive_feature,visit_number)
    
    # check positive features first, get the id for patients who has non nan data for positive features
    positive_id = df[df[positive_feature].notna().any(axis=1)].index
    
    # check negative case to see if we can revert the decision, 
    # if patients with positive_id shows no negative sign, record the ids
    negative_df = df.loc[positive_id][negative_feature]
    true_positive_ids = negative_df[~negative_df[negative_feature].notna().any(axis=1)].index
    
    if visit_number==2 or visit_number=="EHR":
        # this df has all patients who has disease and doesn't have negative features
        positive_df = df.loc[true_positive_ids,positive_feature]
        # merge with the CMR image date, to check if any positive feature is before the CMR image
        positive_df = positive_df.merge(recruit_df,left_index=True,right_on="eid",how="left").set_index("eid")
        # check any date in these positive features are before recruit_date
        positive_df= positive_df.apply(pd.to_datetime, errors='coerce')

        is_earlier = positive_df.apply(lambda x: x < positive_df['recruit_date'], axis=0)
        
        rows_with_earlier_dates = is_earlier.any(axis=1)
        filtered_df = positive_df[rows_with_earlier_dates]
        true_positive_ids = filtered_df.index
        
    df_merged =  df.merge(recruit_df,left_index=True,right_on="eid",how="left").set_index("eid") 
    return df_merged.loc[true_positive_ids,negative_feature+positive_feature+["recruit_date"]].index

def filtering_MI(df,recruit_df, negative_feature:list,positive_feature:list,visit_number)->pd.DataFrame:
    """
    This function tries to filter according to negative and positive features.
    If any negative features are not nan, then, check positive features. If non positive
    features existed, then it is prevalent case
    """
    negative_feature,positive_feature = add_visit_info(negative_feature,positive_feature,visit_number)
    
    # check positive features first, get the id for patients who has non nan data for positive features
    positive_id = df[df[positive_feature].notna().any(axis=1)].index

    
    if visit_number==2 or visit_number=="EHR":
        # this df has all patients who has disease and doesn't have negative features
        positive_df = df.loc[positive_id,positive_feature]
        # merge with the CMR image date, to check if any positive feature is before the CMR image
        positive_df = positive_df.merge(recruit_df,left_index=True,right_on="eid",how="left").set_index("eid")
        # check any date in these positive features are before recruit_date
        positive_df= positive_df.apply(pd.to_datetime, errors='coerce')
        is_earlier = positive_df.apply(lambda x: x < positive_df['recruit_date'], axis=0)
        rows_with_earlier_dates = is_earlier.any(axis=1)
        filtered_df = positive_df[rows_with_earlier_dates]
        positive_id = filtered_df.index
        
    df_merged =  df.merge(recruit_df,left_index=True,right_on="eid",how="left").set_index("eid") 
    return df_merged.loc[positive_id,positive_feature+["recruit_date"]].index
