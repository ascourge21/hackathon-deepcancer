% Takes a CT series in a folder without file extensions
% Sorts, Anonymizes and writes files into new folder.

clear all
close all
clc

[FileName,PathName] = uigetfile('*.*','Select any Dicom file');
files = dir(strcat(PathName,'*'));

countr = 1; % counter
for k = 1:numel(files);  
    try reader = dicominfo(strcat(PathName, files(k).name));
        listr(countr,1) = reader.InstanceNumber;
        listr(countr,2) = k;
        countr = countr + 1;
    catch err % ignore all errors
%'error'
    end
end

listr = sortrows(listr,1); % order the files in listr

PathNameout = strcat((PathName(1:end-1)), '0', '/');
mkdir(PathNameout);
lvar = 1001;

for k2 = 1: (countr-1);
    dcm = dicomread(strcat(PathName, files(listr(k2,2)).name));
    dicomwrite(dcm, strcat(PathNameout, num2str(lvar),'.dcm'));
    
read = dicomread(strcat(PathNameout, num2str(lvar),'.dcm'));
imshow(read, [])
pause(0.1)

    lvar = lvar + 1;
end

%close all force

'done'