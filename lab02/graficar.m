pkg load io
data = csv2cell('market-price.csv');

ycell = data(2:end,2);
y = cell2mat(ycell);

datetime = data(2:end,1);
mydate = cellfun(@(x) strsplit(x){1}, datetime,'uniformoutput',false);

xindex = round(linspace(1,366,8));

y2 = movmean(y,7);

plot(y2,'LineWidth',1);
set(gca, 'xtick', xindex,"fontsize", 15);
grid();
titulo = "Precio semanal de Bitcoin durante el ultimo año.";
title(titulo,'fontsize',25);
ylabel("Precio en $",'fontsize',20);
xlabel("Fecha",'fontsize',20);
xticklabels(mydate(xindex))
#yticklabels({'min','y = 0','max'})