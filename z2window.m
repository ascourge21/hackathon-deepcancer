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

matr = uint8(zeros(512,512*(countr-1)));
dcm2 = uint8(zeros(512,512));

for k2 = 1: (countr-1);
    dcm = dicomread(strcat(PathName, files(listr(k2,2)).name));
%    dicomwrite(dcm, strcat(PathNameout, num2str(lvar),'.dcm'));
    dcm2 = uint8(dcm*256/400);
    matr(:,((k2-1)*512)+1:((k2-1)*512)+512) = dcm2;
%    lvar = lvar + 1
end

imwrite(matr, strcat(PathName(1:26),'jpg/',PathName(41:end-1),'.jpg'));

'done'
