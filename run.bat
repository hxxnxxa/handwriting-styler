REM python src-font-image-generator.py
REM python tgt-font-image-generator.py
REM python combine-images.py --input_dir src-image-data/images --b_dir tgt-image-data/images --operation combine
REM python images-to-tfrecords.py
REM python images-to-tfrecords.py
REM python main.py --mode train --output_dir trained_model --max_epochs 100
REM python test-images-to-tfrecords.py
REM python main.py --mode test --output_dir testing --checkpoint trained_model
REM python main.py --mode train --output_dir finetuned_model --max_epochs 100 --checkpoint trained_model
REM python main.py --mode test --output_dir testing --checkpoint finetuned_model
REM -------------------------------------------------------------------------------------------------------------------- second trial :)
REM python src-font-image-generator.py
REM python tgt-font-image-generator.py
REM python combine-images.py --input_dir src-image-data/images --b_dir tgt-image-data/images --operation combine
REM python images-to-tfrecords.py
REM python main.py --mode train --output_dir trained_model-modified --max_epochs 100
REM python test-images-to-tfrecords.py
REM python main.py --mode test --output_dir testing-modified --checkpoint trained_model
REM python main.py --mode train --output_dir finetuned_model-modified --max_epochs 100 --checkpoint trained_model
REM python main.py --mode test --output_dir testing-modified --checkpoint finetuned_model
REM -------------------------------------------------------------------------------------------------------------------- third trial :)
REM python src-font-image-generator.py
REM python tgt-font-image-generator.py
REM python combine-images.py --input_dir src-image-data/images --b_dir tgt-image-data/images --operation combine
REM python images-to-tfrecords.py
python main.py --mode train --output_dir trained_model-modified --max_epochs 100
python test-images-to-tfrecords.py
python main.py --mode test --output_dir testing-modified --checkpoint trained_model
python main.py --mode train --output_dir finetuned_model-modified --max_epochs 100 --checkpoint trained_model
python main.py --mode test --output_dir testing-modified --checkpoint finetuned_model