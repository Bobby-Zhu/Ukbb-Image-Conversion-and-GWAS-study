# Copyright 2017, Wenjia Bai. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""
    This script demonstrates a pipeline for cardiac MR image analysis.
"""
import os
import urllib.request
import shutil
from datetime import datetime
import sys

if __name__ == '__main__':
    
    foldnum = sys.argv[1];
    # Get the current time
    start_time = datetime.now()
    
    # The GPU device id
    CUDA_VISIBLE_DEVICES = 0
    URL = 'https://www.doc.ic.ac.uk/~wbai/data/ukbb_cardiac/'

    # Download trained models
    print('Downloading trained models ...')
    if not os.path.exists('trained_model'):
        os.makedirs('trained_model')
    for model_name in ['FCN_sa', 'FCN_la_2ch', 'FCN_la_4ch', 'FCN_la_4ch_seg4', 'UNet-LSTM_ao']:
        for f in ['trained_model/{0}.meta'.format(model_name),
                  'trained_model/{0}.index'.format(model_name),
                  'trained_model/{0}.data-00000-of-00001'.format(model_name)]:
            urllib.request.urlretrieve(URL + f, f)

    data_root = "/mnt/stsi/stsi3/Internal/ukbb_cardiac/"
    output_root = os.path.join(data_root,'output_csv')
    if not os.path.exists(output_root):
        os.mkdir(output_root)
    # path to bloodpressure file
    blood_pressure_dir = os.path.join(data_root,"test","input")
    

    list_error = []

    
    input_dir = os.path.join(data_root,"nifti",foldnum)
    # input_dir = os.path.join(data_root,"input",foldnum,str(eid))        
    output_dir = os.path.join(output_root,foldnum)
    if not os.path.exists(output_dir):
            os.mkdir(output_dir)


    #     # Analyse aortic images
    print('******************************')
    print('  Aortic image analysis')
    print('******************************')

    # Deploy the segmentation network
    print('Deploying the segmentation network ...')
    os.system(f'CUDA_VISIBLE_DEVICES={0} python3 common/deploy_network_ao.py --seq_name ao --data_dir {input_dir} --model_path trained_model/UNet-LSTM_ao'.format(CUDA_VISIBLE_DEVICES))

    # Evaluate aortic areas
    print('Evaluating atrial areas ...')
    os.system(f'python3 aortic/eval_aortic_area.py --data_dir {input_dir} --pressure_csv {blood_pressure_dir}/blood_pressure_info.csv --output_csv {output_dir}/table_aortic_area.csv')
    
    
    print('Done.')
    
    # Format the current time as a string (optional)
    formatted_time = start_time.strftime("%Y-%m-%d %H:%M:%S")

    # Print the current time
    print("Start time:", formatted_time)
    
    # Get the current time
    end_time = datetime.now()

    # Format the current time as a string (optional)
    formatted_time = end_time.strftime("%Y-%m-%d %H:%M:%S")

    # Print the current time
    print("End time:", formatted_time)
