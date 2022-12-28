started at December 23th Friday, 2022

<div align='center'>
    <h1>Generate user`s handwriting style</h1>
</div>

<h2>1. Environment</h2>
<li>Tensorflow 1.15 (GPU version)</li>

<br>

<h2>2. How to use</h2>

<b>2-1. Generate Source Images</b>

```python
python src-font-image-generator.py
```

<b>2-2. Generate Target Images</b>

```python
python tgt-font-image-generator.py
```

<b>2-3. Combine source images with target images</b>

```python
python combine-images.py --input_dir src-image-data/images --b_dir tgt-image-data/images --operation combine
```

<b>2-4. Convert images to TFRecord file</b>

```python
python images-to-tfrecords.py
```

<b>2-5. Train the model</b>

```python
python main.py --mode train --output_dir trained_model --max_epochs 100
```

<b>2-6. Convert trained images to TFRecord file</b>

```python
python test-images-to-tfrecords.py
```

<b>2-7. Generate testing results</b>

```python
python main.py --mode test --output_dir testing --checkpoint trained_model
```

<b>2-8. Finetune the model</b>

```python
python main.py --mode train --output_dir finetuned_model --max_epochs 100 --checkpoint trained_model
```

<b>2-9. Testing results of finetuned model</b>

```python
python main.py --mode test --output_dir testing --checkpoint finetuned_model
```