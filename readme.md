# ALL SUBSET SUM BY FFT
This project uses python to implement the algorithm for calculating all subset sum problems using fft [(view paper here)](https://arxiv.org/abs/1807.08248).

The algorithm introduced in the paper has $O(\sqrt{n}t)$ time complexity, while after verification in this project, we concluded that the running time is only proprotional to n.

## Dependencies

Install dependencies by this command.If you only want to run this project on cpu, before installing, edit `requirements.txt` to delete tensorflow. Tested on `python 3.11.5`

```bash
pip install -r requirements.txt
```

GPU tested on `python 3.9.18`

There are two notebook file in `notebook`. Thus Jupyter is recommanded, but not necessary.

## Quick Start

```python
from src import ALLSUBSETSUMS
# example
ALLSUBSETSUMS(np.array([1,4,6,7,9,10]),10)
```

If you want to test the algorithm, run this command

```bash
cd test
python test.py 
```

<a name='test.py-introduction'></a>
This script will validate correctness of the algorithm, printing success if all sample passed. All samples will be recorded in `data/fft-subset_sum-n`.
Then, it will record runtime-n-t data to `experiment/fft-subset_sum-device-n-t-distribution-parameterOfDistribution.txt`, with similar naming format, generate `*-n-time.png` and `*-t-time.png`.

Adjustable parameters can be easily accessed in `test.py`,  below `#*`.

## Quick View

This project defaults to using CPU, if you want to use gpu, edit `src/config.py`, and change `device` into `gpu`

If you don't have Jupyter, skip to [python script](#Python-Script)

### Jupyter

The core of this project is briefly implemented in `notebook` . `subset_sum.ipynb` implements the whole algorithm, and `test.ipynb` tests correctness and runtime of the algorithm.




<a name="Python-Script"></a>
### Python Script

Scripts for implementing the algorithm are in `src`.

The `math_operations.py` mainly implements 1-dimension and 2-dimension _Polynomial Multiplication Using fft_ and *Minscowsky Sum*. `fft_subset_sum.py` imports it and completes the algorithm.

`bt_subset_sum.py` solves the problem by backtrace, which is used to test correctness of the algorithm.

In `test`, there is a `test.py` script, which has been introduced [above](#test.py-introduction). The script file is brief, by importing `tools.py` , which is easy for others to modify parameters.

