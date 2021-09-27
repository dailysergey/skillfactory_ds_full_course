# Skillfactory full course final

### [BirdCLEF 2021 - Birdcall Identification](https://www.kaggle.com/c/birdclef-2021)
#### Identify bird calls in soundscape recordings

#### Описание задачи
Во всем мире насчитывается более 10 000 видов птиц. Например, идентификация дроздов в регионе может предоставить важную информацию об ареале обитания. Поскольку птицы занимают высокую позицию в пищевой цепочке, они являются отличным индикатором ухудшения качества окружающей среды и загрязнения. Мониторинг состояния и тенденций биоразнообразия в экосистемах - непростая задача.
#### Описание данных
Задача в этом соревновании - определить, какие птицы поют на​ аудиозаписях, полученные из разных регионов. Такое соревнование не первое, это соревнование отличается записями из новых мест, большим видов птиц. 397 видов птиц - соответственно классов. Записи могут содержать несколько файликов, поэтому в есть primary label, secondary label. Могу предположить, что для этого организаторы предложили в качестве метрики использовать микро усредненная по строка f1-score. На выходе submission файл с указанием строки из test-ого файла и через пробел указанием списка птиц, которые попали в файл.
#### Ход решения
* Использовал подготовленые 5 датасетов для обучения с mel-спектограммами, разбитые на 5 фолдов
* Использовал с прошлого соревнования мета файл с ручной разметкой файликов, в которых есть исправления secondary labels
* Аугментация
* Использовал resnest50, resnext, efficientnet-b0
* Blend с разными thresholds