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
    # print(input_dir)


    # Find demo images
    print('Findng demo images ...')

    
# Analyse show-axis images
    print('******************************')
    print('  Short-axis image analysis')
    print('******************************')

    # Deploy the segmentation network
    print('Deploying the segmentation network ...')
    os.system(f'CUDA_VISIBLE_DEVICES={CUDA_VISIBLE_DEVICES} python3 common/deploy_network.py --seq_name sa --data_dir {input_dir} --model_path trained_model/FCN_sa')


    # Evaluate ventricular volumes
    print('Evaluating ventricular volumes ...')
    os.system(f'python3 short_axis/eval_ventricular_volume.py --data_dir {input_dir} --output_csv {output_dir}/table_ventricular_volume.csv')

    # Evaluate wall thickness
    print('Evaluating myocardial wall thickness ...')
    os.system(f'python3 short_axis/eval_wall_thickness.py --data_dir {input_dir} --output_csv {output_dir}/table_wall_thickness_volume.csv')

    # Evaluate strain values
    if shutil.which('mirtk'):
        print('Evaluating strain from short-axis images ...')
        os.system(f'python3 short_axis/eval_strain_sax.py --data_dir {input_dir} --par_dir par --output_csv {output_dir}/table_strain_sax.csv')




    # Analyse long-axis images
    print('******************************')
    print('  Long-axis image analysis')
    print('******************************')

    # Deploy the segmentation network
    print('Deploying the segmentation network ...')
    os.system(f'CUDA_VISIBLE_DEVICES={0} python3 common/deploy_network.py --seq_name la_2ch --data_dir {input_dir} --model_path trained_model/FCN_la_2ch'.format(CUDA_VISIBLE_DEVICES))

    os.system(f'CUDA_VISIBLE_DEVICES={0} python3 common/deploy_network.py --seq_name la_4ch --data_dir {input_dir} --model_path trained_model/FCN_la_4ch'.format(CUDA_VISIBLE_DEVICES))

    os.system(f'CUDA_VISIBLE_DEVICES={0} python3 common/deploy_network.py --seq_name la_4ch --data_dir {input_dir} --seg4 --model_path trained_model/FCN_la_4ch_seg4'.format(CUDA_VISIBLE_DEVICES))

    # Evaluate atrial volumes
    print('Evaluating atrial volumes ...')
    os.system(f'python3 long_axis/eval_atrial_volume.py --data_dir {input_dir} --output_csv {output_dir}/table_atrial_volume.csv')

    # Evaluate strain values
    if shutil.which('mirtk'):
        print('Evaluating strain from long-axis images ...')
        os.system(f'python3 long_axis/eval_strain_lax.py --data_dir {input_dir} --par_dir par --output_csv {output_dir}/table_strain_lax.csv')

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
