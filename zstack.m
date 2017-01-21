% Takes a folder of Anonymized BMP files and writes all files into PNG

clear all
close all
clc

% INPUTS IN XY NOTATION
topL = [149,163]; botR = [387,418];   % cine MRI
%topL = [93,124]; botR = [681,546];   % parathyroid
%topL = [150,107]; botR = [692,561]; % tvus 
%topL = [122,100]; botR = [679,573];  % seb cyst axial
%topL = [122,100]; botR = [695,544];  % seb cyst sag
%topL = [147,86]; botR = [694,542];  % thyroid
%topL = [248,102]; botR = [604,450];  % pop fossa cyst
%topL = [120,165]; botR = [675,556];  % fetal 

% ALTERNATES ONLY
alt = 1;


[FileName,PathName] = uigetfile('*.bmp','Select file',...
 '/Users/g/Documents/Images/raw/');
files = dir(strcat(PathName,'/*'));
PathNameout = strcat(PathName(1:end-3));

fr = botR(2) - topL(2) + 1;
fc = botR(1) - topL(1) + 1;
fz = floor((numel(files)-2)/alt);

fcount = 1001;

lvar2 = 1;

final = uint8(zeros(fr,(fc*fz)));
%for lvar = 10:fz-10; 
%final = uint8(zeros(fr,(fc*80)));

%for lvar = 1:2:160; 
    
for lvar = 1:alt:(fz*alt);    % crop from side to side essentially
    reader = imread(strcat(PathName, '/', num2str(fcount+lvar-1), '.bmp'));
    % Darken specific parts of image
    %reader(525:end, 650:end) = 0;
    final(:,lvar2:(lvar2+fc-1)) = reader(topL(2):botR(2),topL(1):botR(1)); 
    lvar2 = lvar2+fc;
end

imwrite(final, strcat(PathNameout, PathName(end-2:end), '.png'),'png');
imwrite(final, strcat(PathNameout, PathName(end-2:end), '.jpg'),'jpg');

'done'
[fc, fr, (size(final,2))/fc, size(final,2), size(final,1)]