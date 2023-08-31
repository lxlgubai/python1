
axios({
  //接口地址
  url:'http://127.0.0.1:5000/opst'
  }).then(res=>{
  // 控制台输出请求结果
  console.log(res)
  });

var idd = document.querySelector('#id111')
console.log(idd)
var idb = (function(){
  axios({
    url:'http://127.0.0.1:5000/opst'
  }).then(thin())
})
axios({
  //接口地址
  url:'http://127.0.0.1:5000/pymysql'
  }).then(res=>{
  // 控制台输出请求结果
  console.log(res)
  });
