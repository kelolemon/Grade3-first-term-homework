const create_scene = () => {
    return new THREE.Scene()
}

const create_camera = (scene) => {
    return new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.01, 2000)
}

const create_renderer = () => {
    const renderer = new THREE.WebGLRenderer()
    renderer.setSize(window.innerWidth, window.innerHeight)
    document.body.appendChild(renderer.domElement)
    return renderer
}

const create_mouse_control = (camera, renderer) => {
    const controls = new THREE.OrbitControls(camera, renderer.domElement)
    controls.enableZoom = true;
    controls.minDistance  = 200;
    controls.maxDistance  = 600;
    controls.enablePan = true;
    return controls
}

function ModernCity (renderer) {
    var cube=new THREE.CubeGeometry(1,1,1);
    cube.applyMatrix(new THREE.Matrix4().makeTranslation(0,0.5,0));   //将参考点设置在立方体的底部
    cube.faces.splice(6, 2);   //去掉立方体的底面
    cube.faceVertexUvs[0].splice(6, 2);
    //去掉顶面的纹理
    cube.faceVertexUvs[0][4][0].set(0, 0);
    cube.faceVertexUvs[0][4][1].set(0, 0);
    cube.faceVertexUvs[0][4][2].set(0, 0);

    cube.faceVertexUvs[0][5][0].set(0, 0);
    cube.faceVertexUvs[0][5][1].set(0, 0);
    cube.faceVertexUvs[0][5][2].set(0, 0);

    let buildingMesh=new THREE.Mesh(cube);

    //楼房
    let buildingMaxW=15;
    let buildingMaxD=15;

    //社区
    let blockNumX=20;
    let blockNumZ=20;
    let blockSizeX=50;
    let blockSizeZ=50;
    let blockDensity= 15;

    //街道
    let roadW=8;
    let roadD=8;

    //人行道
    let sidewayW=2;
    let sidewayH=0.3;
    let sidewayD=2;

    // 生成纹理
    let buildingTexture=new THREE.Texture(generateTextureCanvas());
    buildingTexture.anisotropy=renderer.getMaxAnisotropy();
    buildingTexture.needsUpdate=true; //在下次使用纹理时触发一次更新

    //建立城市
    let object=new THREE.Object3D();

    let groundMesh=createSquareGround();
    groundMesh.castShadow=true;
    groundMesh.receiveShadow=true;
    object.add(groundMesh);

    let sidewayMesh=createSquareSideWay();
    sidewayMesh.castShadow=true;
    sidewayMesh.receiveShadow=true;
    object.add(sidewayMesh);

    let buildingsMesh=createSquareBuildings();
    buildingsMesh.castShadow=true;
    buildingsMesh.receiveShadow=true;
    object.add(buildingsMesh);

    return object;

    function createSquareGround() {
        //建立地面
        let geometry=new THREE.PlaneGeometry(1,1,1);
        let material=new THREE.MeshLambertMaterial({color:0x222222});
        let ground=new THREE.Mesh(geometry,material);
        ground.rotation.x = (-90 * Math.PI) / 180;
        ground.scale.x=blockNumX*blockSizeX;
        ground.scale.y=blockNumZ*blockSizeZ;
        ground.receiveShadow=true;
        return ground;
    }

    function createSquareSideWay() {
        let sidewayGeometry=new THREE.Geometry();

        for(let i=0;i<blockNumZ;i++){
            for(let j=0;j<blockNumX;j++){
                //选取初始坐标
                buildingMesh.position.x=(i+0.5-blockNumX/2)*blockSizeX;
                buildingMesh.position.z=(j+0.5-blockNumZ/2)*blockSizeZ;

                //初始化大小
                buildingMesh.scale.x=blockSizeX-roadW;
                buildingMesh.scale.y=sidewayH;
                buildingMesh.scale.z=blockSizeZ-roadD;

                //加入城市
                buildingMesh.updateMatrix();
                sidewayGeometry.merge(buildingMesh.geometry, buildingMesh.matrix);
            }
        }
        let material=new THREE.MeshLambertMaterial();
        material.map=buildingTexture;
        material.vertexColors=THREE.VertexColors;
        let sidewayMesh=new THREE.Mesh(sidewayGeometry,material);
        return sidewayMesh;

    }


    function createSquareBuildings() {
        //建立楼房
        let cityGeometry=new THREE.Geometry();

        for(let i=0;i<blockNumZ;i++){
            for(let j=0;j<blockNumX;j++){
                for(let k=0;k<blockDensity;k++){
                    //随机选取楼房初始坐标
                    buildingMesh.position.x=Math.floor((Math.random()-0.5)*(blockSizeX-buildingMaxW-roadW-sidewayW));//在-1000到1000之间
                    buildingMesh.position.z=Math.floor((Math.random()-0.5)*(blockSizeZ-buildingMaxD-roadD-sidewayD));

                    buildingMesh.position.x=buildingMesh.position.x+(j+0.5-blockNumX/2)*blockSizeX;
                    buildingMesh.position.z=buildingMesh.position.z+(i+0.5-blockNumZ/2)*blockSizeZ;
                    //console.log(buildingMesh.position);


                    //随机初始化楼房大小
                    buildingMesh.scale.x=Math.min(Math.random() * Math.random()* 5 + 10, buildingMaxW);
                    buildingMesh.scale.y=(Math.random() * Math.random() * Math.random() * buildingMesh.scale.x) * 3 + 8;
                    buildingMesh.scale.z=Math.min(buildingMesh.scale.x,buildingMaxD);

                    //随机初始化楼房的颜色
                    let value=1-Math.random()*Math.random();
                    let basicColor=new THREE.Color().setRGB(value+0.2*Math.random(),value,value+0.2*Math.random());

                    //逐面添加颜色
                    let geometry=buildingMesh.geometry;
                    for (let m=0, jmax=geometry.faces.length; m<jmax; m++){
                        geometry.faces[m].vertexColors = [basicColor, basicColor, basicColor];
                    }

                    //将楼房加入城市
                    buildingMesh.updateMatrix();
                    cityGeometry.merge(buildingMesh.geometry, buildingMesh.matrix);
                }
            }
        }
        let material=new THREE.MeshLambertMaterial();
        material.map=buildingTexture;
        material.vertexColors=THREE.VertexColors;
        let cityMesh=new THREE.Mesh(cityGeometry,material);
        return cityMesh;
    }
}


function generateTextureCanvas(){
    let canvas = document.createElement('canvas');
    canvas.width=16;
    canvas.height=32;
    var context=canvas.getContext( '2d' );
    context.fillStyle = '#ffffff';
    context.fillRect(0, 0, 32, 64);

    //画窗户
    for(let y=2;y<32;y+=2){
        for(let x=0;x<16;x+=2){
            var value=Math.floor(Math.random()*64);
            context.fillStyle='rgb('+[value,value,value].join(',')+')';
            context.fillRect(x,y,2,1);
        }
    }

    let canvas2=document.createElement('canvas');
    canvas2.width=512;
    canvas2.height=1024;
    var context=canvas2.getContext('2d');

    context.imageSmoothingEnabled=false;
    context.webkitImageSmoothingEnabled=false;
    context.mozImageSmoothingEnabled=false;

    context.drawImage(canvas,0,0,canvas2.width,canvas2.height);
    return canvas2;
}

const init = () => {
    const scene = create_scene()
    const camera = create_camera(scene)
    const renderer = create_renderer()
    const mouse_control = create_mouse_control(camera, renderer)
    let move_forward = false
    let move_back = false
    let move_right = false
    let move_left = false
    const on_resize = () => {
        camera.aspect = window.innerWidth / window.innerHeight
        camera.updateProjectionMatrix()
        renderer.setSize(window.innerWidth, window.innerHeight)
    }
    window.addEventListener('resize', on_resize, false)

    //
    let spotLight=new THREE.SpotLight(0xffffcc);
    spotLight.position.set(200, 150, 0);
    spotLight.castShadow=true;
    scene.add(spotLight);
    // 添加球体
    let geometry = new THREE.SphereGeometry( 5, 32, 32 );
    let material = new THREE.MeshBasicMaterial( {color: 0xCC0000} );
    let sphere = new THREE.Mesh( geometry, material );
    sphere.position.set(200, 150, 0);
    scene.add(sphere);

// 打开renderer开关
    renderer.shadowMap.enabled=true;
    renderer.shadowMap.type=THREE.PCFSoftShadowMap;
    camera.position.x = 0;
    camera.position.y = 50;
    camera.position.z = 30;
    const city=new ModernCity(renderer);
    city.castShadow=true;
    city.receiveShadow=true;
    scene.add(city);

    camera.position.set(-20, 0, 0);
    camera.lookAt(scene.position);
    scene.add(camera);


    let controls;
    let moveForward = false;
    let moveBackward = false;
    let moveLeft = false;
    let moveRight = false;
    let canJump = false;
    let spaceUp = true;
    let prevTime = performance.now();
    let velocity = new THREE.Vector3(0, 0, 0);
    let direction = new THREE.Vector3(0, 0, 0);
    let rotation = new THREE.Vector3(0, 0, 0);
    let upRaycaster, downRaycaster, horizontalRaycaster, horizontalRaycasterF;
    const speed = 1000;
    const upSpeed = 500;
    const [sizeW, sizeH, segW, segH] = [60, 40, 24, 16];
    let flags = [];

    function initPointerLockControls() {
        controls = new THREE.PointerLockControls( camera, document.body );
        // 设置第一人称的初始位置，需要与后面相对应
        controls.getObject().position.set(760, -120, -2470);
        scene.add(controls.getObject());

        const blocker = document.getElementById('blocker');
        const instructions = document.getElementById('instructions');
        const havePointerLock =
            'pointerLockElement' in document ||
            'mozPointerLockElement' in document ||
            'webkitPointerLockElement' in document;
        if (havePointerLock) {
            instructions.addEventListener(
                'click',
                function() {
                    controls.lock();
                },
                false
            );
            controls.addEventListener('lock', function() {
                instructions.style.display = 'none';
                blocker.style.display = 'none';
            })
            controls.addEventListener('unlock', function() {
                blocker.style.display = 'block';
                instructions.style.display = '';
            })
        } else {
            instructions.innerHTML =
                'Your browser does not support Pointer Lock API, please change your browser';
        }

        const onKeyDown = function(event) {
            switch (event.keyCode) {
                case 38: // up
                case 87: // w
                    moveForward = true;
                    break;
                case 37: // left
                case 65: // a
                    moveLeft = true;
                    break;
                case 40: // down
                case 83: // s
                    moveBackward = true;
                    break;
                case 39: // right
                case 68: // d
                    moveRight = true;
                    break;
                case 32: // space
                    if (canJump && spaceUp) velocity.y += upSpeed; //垂直初速度
                    canJump = false;
                    spaceUp = false;
                    break;
            }
        }
        const onKeyUp = function(event) {
            switch (event.keyCode) {
                case 38: // up
                case 87: // w
                    moveForward = false;
                    break;
                case 37: // left
                case 65: // a
                    moveLeft = false;
                    break;
                case 40: // down
                case 83: // s
                    moveBackward = false;
                    break;
                case 39: // right
                case 68: // d
                    moveRight = false;
                    break;
                case 32: // space
                    spaceUp = true;
                    break;
            }
        }
        document.addEventListener('keydown', onKeyDown, false);
        document.addEventListener('keyup', onKeyUp, false);

        // 使用 Raycaster 实现简单碰撞检测
        downRaycaster = new THREE.Raycaster(new THREE.Vector3(0, 0, 0), new THREE.Vector3(0, -1, 0), 0, 10);
        horizontalRaycaster = new THREE.Raycaster(new THREE.Vector3(0, 0, 0), new THREE.Vector3(0, 0, 0), 0, 10);
        horizontalRaycasterF = new THREE.Raycaster(new THREE.Vector3(0, 0, 0), new THREE.Vector3(0, 0, 0), 0, 10);
    }

    function pointerLockControlsRender() {
        const time = performance.now();

        if ( controls.isLocked === true ) {
            //获取控制器对象
            const control = controls.getObject();
            //获取刷新时间
            const delta = ( time - prevTime ) / 1000;

            //velocity为每次的速度，为了保证有过渡
            velocity.x -= velocity.x * 10.0 * delta;
            velocity.z -= velocity.z * 10.0 * delta;
            velocity.y -= 9.8 * 100.0 * delta; // 100.0 = mass

            //获取当前按键的方向并获取朝哪个方向移动
            //向前移动，z值（代表前后方向）为1，向后移动，z值为-1
            direction.z = (Number( moveForward ) - Number( moveBackward ));
            //向右移动，x值（代表前后方向）为1，向左移动，x值为-1
            direction.x = (Number( moveRight ) - Number( moveLeft ));
            //将法向量的值归一化
            direction.normalize();

            //判断是否接触到了模型
            let vec = new THREE.Vector3(0, 0, 0);
            // .getWorldDirection ( target : Vector3 ) : Vector3
            // target — 调用该函数的结果将复制给该Vector3对象。
            // 返回一个能够表示当前摄像机所  正视的 世界空间方向的Vector3对象。 （注意：摄像机俯视时，其Z轴坐标为负。）
            control.getWorldDirection(vec);
            //乘上一个矩阵消除y轴上的值，这样仰视的时候和平视一样处理，碰到阻挡一样过不去
            let rotationF = new THREE.Vector3(0, 0, 0).copy(rotation);
            let vecF = new THREE.Vector3(0, 0, 0).copy(vec);
            rotation.copy(vec.multiply(new THREE.Vector3(-1, 0, -1))); //左右方向碰撞检测
            rotationF.copy(vecF.multiply(new THREE.Vector3(1, 0, 1))); //前后方向碰撞检测

            //判断鼠标按下的方向
            const m = new THREE.Matrix4();

            if(direction.z > 0){
                if(direction.x > 0)
                    m.makeRotationY(Math.PI/4);
                else if(direction.x < 0)
                    m.makeRotationY(-Math.PI/4);
                else
                    m.makeRotationY(0);
            }
            else if(direction.z < 0) {
                if (direction.x > 0)
                    m.makeRotationY(Math.PI / 4 * 3);
                else if (direction.x < 0)
                    m.makeRotationY(-Math.PI / 4 * 3);
                else
                    m.makeRotationY(Math.PI);
            }
            else{
                if(direction.x > 0)
                    m.makeRotationY(Math.PI/2);
                else if(direction.x < 0)
                    m.makeRotationY(-Math.PI/2);
            }
            //给向量使用变换矩阵
            rotation.applyMatrix4(m);
            rotationF.applyMatrix4(m);

            //这个水平方向的向量现在与第一人称的方向一致
            horizontalRaycasterF.set( control.position , rotationF );
            horizontalRaycaster.set( control.position , rotation );

            let horizontalIntersections = horizontalRaycaster.intersectObjects( scene.children, true );
            const horOnObject = horizontalIntersections.length > 0;
            let horizontalIntersectionsF = horizontalRaycasterF.intersectObjects( scene.children, true );
            const horOnObjectF = horizontalIntersectionsF.length > 0;

            //判断移动方向修改速度方向
            if(!horOnObject){
                //if ( moveForward || moveBackward ) velocity.z -= direction.z * speed * delta;
                if ( moveLeft || moveRight ) velocity.x -= direction.x * speed * delta;
            }

            if(!horOnObjectF){
                if ( moveForward || moveBackward ) velocity.z -= direction.z * speed * delta;
                //if ( moveLeft || moveRight ) velocity.x -= direction.x * speed * delta;
            }

            //复制相机的位置
            downRaycaster.ray.origin.copy( control.position );
            //获取相机靠下10的位置
            downRaycaster.ray.origin.y -= 10;
            //判断是否停留在了立方体上面
            //intersections.length物体上表面的高度减去down射线端点的高度，由于down射线是(0,-1,0)，当控制器在物体上表面上，射线会穿进表面
            //所以intersections.length会大于零，因此可以跳，
            const intersections = downRaycaster.intersectObjects( scene.children, true );
            const onObject = intersections.length > 0;

            if ( onObject === true ) {
                velocity.y = Math.max( 0, velocity.y );
                canJump = true;
            }

            // new behavior
            controls.moveRight(  -velocity.x * delta );
            controls.moveForward(  -velocity.z * delta );
            control.position.y += ( velocity.y * delta );

            //防止第一人称跑到地板下
            if ( control.position.y < -120 ) {
                velocity.y = 0;
                control.position.y = -120;
                canJump = true;
            }
        }
        prevTime = time;
    }

    initPointerLockControls();

    function render() {
        requestAnimationFrame(render);

        const h = 0.5, v = 0.5, w = 0.5, s = 0.5;
        for (let i = 0; i < flags.length; i++) {
            for (let y = 0; y < segH + 1; y++) {
                for (let x = 0; x < segW + 1; x++) {
                    const index = x + y * (segW + 1);
                    const vertex = flags[i].geometry.vertices[index];
                    const time = Date.now() * s / 100;
                    vertex.z = Math.sin(h * x + v * y - time) * w * x / 4;
                }
            }
            flags[i].geometry.verticesNeedUpdate = true;
        }
        pointerLockControlsRender();
        renderer.render(scene, camera);
    }
    render()

}