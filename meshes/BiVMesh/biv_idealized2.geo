SetFactory("OpenCASCADE");

//R = DefineNumber[ 1.4 , Min 0.1, Max 2, Step 0.01,
//  Name "Parameters/Box dimension" ];
//Rs = DefineNumber[ R*.7 , Min 0.1, Max 2, Step 0.01,
//  Name "Parameters/Cylinder radius" ];
//Rt = DefineNumber[ R*1.25, Min 0.1, Max 2, Step 0.01,
//  Name "Parameters/Sphere radius" ];

//h = 2.00;
//h = 0.9;
h = 0.8;
//h = 0.6;

LVirad = 2.0;
LVthick = 1.13;
LVolength = 8.3;

LVorad = LVirad + LVthick;
LVilength = LVolength - 0.5*LVthick;

RV_offset = 2.0;
RVirad = 3.0 + LVthick/2 - LVthick/3;
RVthick = LVthick/3;
RVolength = 7.0;
RVi2rad = RVirad;


RVorad = RVirad + RVthick;
RVilength = RVolength - RVthick;
RVo2rad = RVi2rad + RVthick;



// Create LV geometry
Box(1) = {0.0, -LVorad, -LVorad, LVolength, 2*LVorad, 2*LVorad};

Sphere(2) = {0.0, 0.0, 0.0, 1.0};
Dilate {{0.0, 0.0 ,0.0}, {LVolength, LVorad, LVorad}}{
	Volume{2};
}

BooleanDifference(3) = {Volume{2}; Delete;}{Volume{1};};

Sphere(4) = {0.0, 0.0, 0.0, 1.0};
Dilate {{0.0, 0.0 ,0.0}, {LVilength, LVirad, LVirad}}{
	Volume{4};
}

BooleanDifference(5) = {Volume{4}; Delete;}{Volume{1}; Delete;};
BooleanDifference(6) = {Volume{3}; Delete;}{Volume{5}; Delete;};


//Box(100) = {0.0, -RVorad+RV_offset, -RVolength, 2*RVorad, 2*RVo2rad, 2*RVolength};
Box(100) = {0.0, -RVorad+RV_offset, -RVo2rad, RVolength, 2*RVorad, 2*RVo2rad};
Sphere(7) = {0.0, RV_offset, 0.0, 1};
//Dilate {{0.0, RV_offset ,0.0}, {RVorad, RVorad, RVolength}}{
Dilate {{0.0, RV_offset ,0.0}, {RVolength, RVorad, RVo2rad}}{
	Volume{7};
}
BooleanDifference(8) = {Volume{7}; Delete;}{Volume{100}; Delete;};

//Box(101) = {0.0, -RVirad+RV_offset, -RVilength, 2*RVirad, 2*RVi2rad, 2*RVilength};
Box(101) = {0.0, -RVirad+RV_offset, -RVi2rad, RVilength, 2*RVirad, 2*RVi2rad};
Sphere(9) = {0.0, RV_offset, 0.0, 1};
//Dilate {{0.0, RV_offset ,0.0}, {RVirad, RVirad, RVilength}}{
Dilate {{0.0, RV_offset ,0.0}, {RVilength, RVirad, RVi2rad}}{
	Volume{9};
}
BooleanDifference(10) = {Volume{9}; Delete;}{Volume{101}; Delete;};
BooleanDifference(11) = {Volume{8}; Delete;}{Volume{10}; Delete;};

Sphere(13) = {0.0, 0.0, 0.0, 1.0};
Dilate {{0.0, 0.0 ,0.0}, {LVolength-0.3, LVorad-0.3, LVorad-0.3}}{
	Volume{13};
}

BooleanDifference(14) = {Volume{11}; Delete;}{Volume{13}; Delete;};


BooleanUnion(15) = {Volume{6}; Delete;}{Volume{14}; Delete;};

Mesh.CharacteristicLengthMin = h;
Mesh.CharacteristicLengthMax = h;

//Physical Surface(1) = {5}; // LV Endo
//Physical Surface(2) = {1,3}; // Epi
//Physical Surface(3) = {6,4}; // RV Endo
//Physical Surface(4) = {2}; // Base
Physical Volume(1) = {15}; // Myocardium 
