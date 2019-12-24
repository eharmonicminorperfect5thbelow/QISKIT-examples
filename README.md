# 量子アルゴリズム
## アルゴリズム一覧
- [ドイチアルゴリズム](https://github.com/solidstatesociety/quantum_algorithm/tree/master/deutsch "deutsch")
- [ドイチジョザアルゴリズム](https://github.com/solidstatesociety/quantum_algorithm/tree/master/deutsch_jozsa "deutsch_jozsa")  
- [ベルンシュタインヴァジラニアルゴリズム](https://github.com/solidstatesociety/quantum_algorithm/tree/master/bernstein_vazirani "bernstein_vazirani")  
## 注意
- 以下の環境で動作確認
  - Python 3.6.6
  - QISKit 0.5.6  
    
  Anaconda3等で仮想環境を作り、そこにインストールすることをオススメします。  
  
  参考サイト
  - Python3.6環境構築(Win環境Anaconda利用)  
  https://qiita.com/kiyoneet/items/f440ac890e1a7a5931e8
  - 量子コンピュータで1+1を計算する[実装編]  
  https://qiita.com/hiroyuki827/items/77b9922ed8acba96df31  
  
  
- ~_real.pyを実行する際は、  
https://quantumexperience.ng.bluemix.net/qx/experience  
のMy Account->Advancedからトークンを取得して(会員登録が必要)、  
コード中のTOKENに取得した文字列を代入してください。  


- ~_real.pyにTOKENを代入してそのまま実行すると実は実機(量子コンピュータ)ではなくIBM Qのシミュレータで実行するようにしてあります。実機で実行したい場合はコード中のBACKENDの値を'ibmqx4'などに変えてください。ibmq_qasm_simulatorでの実行は数秒で終わりますが、実機はかなりの時間(30分以上)がかかります。

- その他参考サイト
  - QISKit SDK 0.5.6 ドキュメント  
  https://qiskit.org/documentation/ja/qiskit.html
  - 量子プログラミング - IBM Q Experience, QISKit 入門 – ClassCat® AI Research  
  http://quantum.classcat.com/
  - qiskit-tutorial  
  https://github.com/QISKit/qiskit-tutorial
  - Python チュートリアル  
  https://docs.python.org/ja/3.6/tutorial/index.html
