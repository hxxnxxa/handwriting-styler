started at December 23th Friday, 2022

<div align='center'>
    <h1>Generate user`s handwriting style</h1>
</div>

<h2>1. Environment</h2>
<li>Tensorflow 1.15 (GPU version)</li>

<br>

<h2>2. How to use</h2>
<h3>2-1. Generate Source Images</h3>

```python
python src-font-image-generator.py
```

<h3>2-2. Generate Target Images</h3>

```python
python tgt-font-image-generator.py
```

<h3>2-3. Combine source images with target images</h3>

```python
python combine-images.py --input_dir src-image-data/images --b_dir tgt-image-data/images --operation combine
```

<h3>2-4. Convert images to TFRecord file</h3>

```python
python images-to-tfrecords.py
```

<h3>2-5. Train the model</h3>

```python
python main.py --mode train --output_dir trained_model --max_epochs 100
```

<h3>2-6. Convert trained images to TFRecord file</h3>

```python
python test-images-to-tfrecords.py
```

<h3>2-7. Generate testing results</h3>

```python
python main.py --mode test --output_dir testing --checkpoint trained_model
```

<h3>2-8. Finetune the model</h3>

```python
python main.py --mode train --output_dir finetuned_model --max_epochs 100 --checkpoint trained_model
```

<h3>2-9. Testing results of finetuned model</h3>

```python
python main.py --mode test --output_dir testing --checkpoint finetuned_model
```