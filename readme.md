started at December 23th Friday, 2022

<br>
<br>

<div align='center'>
    <h1>Generate user`s handwriting style</h1>
</div>

<h2>Introduction</h2>
한글은 실생활에 사용되는 상용 한글은 2,350자이고 자모음의 조합으로 만들 수 있는 모든 글자는 총 11,172자 이다. 이러한 한글의 특성 때문에 한글 폰트를 만드는 일은 많은 시간과 비용이 드는 전문적인 작업이라 알려져 있다. 이러한 한계를 극복하기 위해 인공지능이 내 손글씨를 학습해서 만들어낼 수 있다면 어떨까? 여기서 소개하는 모델은 사용자의 글씨의 특징을 잘 학습해서 비슷한 스타일의 다른 글자들을 생성한다.

<br>
<br>

<h2>Architecture</h2>
<img src="architecture\architecture.png"/>

<br>
<br>

<h2>Development Environment</h2>
<li>Operating System : Window 10</li>
<li>GPU : NVIDIA GeForce GTX 1660 Ti</li>
<li>GPU Library : cuda 10.0, cudnn 7.6.0</li>
<li>Deep Learning Framework : Tensorflow 1.15 (GPU version)</li>

<br>
<br>

<h2>How to use</h2>
<h3>1) Pretraining</h3>

<b>Generate Source Images</b>

```python
python src-font-image-generator.py
```

<b>Generate Target Images</b>

```python
python tgt-font-image-generator.py
```

<b>Combine source images with target images</b>

```python
python combine-images.py --input_dir src-image-data/images --b_dir tgt-image-data/images --operation combine
```

<b>Convert images to TFRecord file</b>

```python
python images-to-tfrecords.py
```

<b>Train the model</b>

```python
python main.py --mode train --output_dir trained_model --max_epochs 100
```

<b>Convert trained images to TFRecord file</b>

```python
python test-images-to-tfrecords.py
```

<b>Generate testing results</b>

```python
python main.py --mode test --output_dir testing --checkpoint trained_model
```

<br>

<h3>2) Finetuning</h3>

<b>Finetune the model</b>

```python
python main.py --mode train --output_dir finetuned_model --max_epochs 100 --checkpoint trained_model
```

<b>Testing results of finetuned model</b>

```python
python main.py --mode test --output_dir testing --checkpoint finetuned_model
```