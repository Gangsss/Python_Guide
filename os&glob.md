
##  OS 모듈


```python
import os
```

### 현재 위치


```python
os.getcwd()
```




    'C:\\Users\\Kim\\Desktop'



### 디렉토리 목록 구하기


```python
os.listdir()
```


```python
# libdir의 변환 값은 리스트 - 파일의 갯수 확인가능해!
files = os.listdir('C:\\Users\\Kim\\Desktop')
```


```python
len(files)
```




    40




```python
type(files)
```




    list




```python
#문자열이 'exe'로 끝나는 경우 출력하기
for x in files:
    if x.endswith('exe'):
        print(x)
```

    chromedriver.exe
    jdk-10.0.2_windows-x64_bin.exe
    

### 디렉토리 바꾸기


```python
os.chdir('/Boaz')
```

## glob


```python
import glob
for filename in glob.glob('*.jpg'):
    print(filename)
```


```python
#재귀적으로 현재 폴더의 하위 폴더까지 탐생하여 확장자가 jpg인 파일 출력
import glob
for filename in glob.iglob('Boaz/**/*.jpg',recursive=True):
    print(filename)
```
