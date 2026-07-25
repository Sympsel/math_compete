function distribution_gui
    % 创建主界面窗口
    f = figure('Name', '常见分布展示与计算', 'Position', [300, 200, 800, 600]);

    % 分布下拉菜单
    uicontrol(f, 'Style', 'text', 'Position', [50, 550, 100, 20], 'String', '选择分布：');
    distMenu = uicontrol(f, 'Style', 'popupmenu', 'Position', [140, 550, 180, 25], ...
        'String', {'1. 二项分布', '2. 泊松分布', '3. 超几何分布', '4. 几何分布', ...
                   '5. 正态分布', '6. 均匀分布', '7. 指数分布', '8. 伽马分布', '9. 贝塔分布'}, ...
        'Callback', @updatePlot);

    % PDF/CDF 单选按钮
    bg = uibuttongroup(f, 'Position', [0.45, 0.93, 0.2, 0.07], 'SelectionChangedFcn', @updatePlot);
    uicontrol(bg, 'Style', 'radiobutton', 'String', 'PDF', 'Position', [10 10 50 20]);
    uicontrol(bg, 'Style', 'radiobutton', 'String', 'CDF', 'Position', [70 10 50 20]);
    bg.SelectedObject = bg.Children(2);  % 默认选中PDF

    % 输入 x
    uicontrol(f, 'Style', 'text', 'Position', [50, 510, 100, 20], 'String', '输入变量 x/k:');
    xInput = uicontrol(f, 'Style', 'edit', 'Position', [140, 510, 100, 25]);

    % 计算按钮
    uicontrol(f, 'Style', 'pushbutton', 'String', '计算 PDF/CDF', ...
        'Position', [260, 510, 120, 25], 'Callback', @calculateResult);

    % 结果显示
    resultText = uicontrol(f, 'Style', 'text', 'Position', [400, 510, 380, 25], 'HorizontalAlignment', 'left');

    % 导出按钮
    uicontrol(f, 'Style', 'pushbutton', 'String', '导出图像', ...
        'Position', [700, 550, 80, 25], 'Callback', @exportImage);

    % 公式显示区域
    global formula_pdf formula_ex formula_var
    formula_pdf = annotation(f, 'textbox', [0.05, 0.7, 0.9, 0.08], ...
        'String', '', 'Interpreter', 'latex', 'EdgeColor', 'none', 'FontSize', 12);
    formula_ex = annotation(f, 'textbox', [0.05, 0.62, 0.9, 0.08], ...
        'String', '', 'Interpreter', 'latex', 'EdgeColor', 'none', 'FontSize', 12);
    formula_var = annotation(f, 'textbox', [0.05, 0.54, 0.9, 0.08], ...
        'String', '', 'Interpreter', 'latex', 'EdgeColor', 'none', 'FontSize', 12);

    % 坐标轴
    ax = axes(f, 'Position', [0.1, 0.1, 0.8, 0.4]);

    updatePlot();  % 初始化绘图

    % ================= 回调函数 =================

    function updatePlot(~, ~)
        val = distMenu.Value;
        isPDF = strcmp(bg.SelectedObject.String, 'PDF');

        switch val
            case 1 % 二项分布
                n = 10; p = 0.5; x = 0:n;
                y = isPDF * binopdf(x, n, p) + ~isPDF * binocdf(x, n, p);
                bar(ax, x, y); title(ax, '1. 二项分布');
                setFormula('$$PDF: C_{n}^{k}p^k(1-p)^{n-k}$$', ...
                           '$$E[X] = np$$', '$$Var[X] = np(1-p)$$');
            case 2 % 泊松分布
                lambda = 3; x = 0:12;
                y = isPDF * poisspdf(x, lambda) + ~isPDF * poisscdf(x, lambda);
                bar(ax, x, y); title(ax, '2. 泊松分布');
                setFormula('$$PDF: \frac{\lambda^k e^{-\lambda}}{k!}$$', ...
                           '$$E[X] = \lambda$$', '$$Var[X] = \lambda$$');
            case 3 % 超几何分布
                N = 50; K = 20; n = 10; x = 0:10;
                y = isPDF * hygepdf(x, N, K, n) + ~isPDF * hygecdf(x, N, K, n);
                bar(ax, x, y); title(ax, '3. 超几何分布');
                setFormula('$$PDF: \frac{C_{M}^{k} C_{N-K}^{n-k}}{C_{N}^{n}}$$', ...
                           '$$E[X] = n \cdot \frac{M}{N}$$', ...
                           '$$Var[X] = n \cdot \frac{M}{N} \cdot \left(1-\frac{M}{N}\right) \cdot \frac{N-n}{N-1}$$');
            case 4 % 几何分布
                p = 0.3; x = 1:15;
                y = isPDF * geopdf(x - 1, p) + ~isPDF * geocdf(x - 1, p);
                bar(ax, x, y); title(ax, '4. 几何分布');
                setFormula('$$PDF: (1-p)^{k-1}p$$', '$$E[X] = 1/p$$', '$$Var[X] = \frac{1-p}{p^2}$$');
            case 5 % 正态分布
                mu = 0; sigma = 1; x = linspace(-5, 5, 1000);
                y = isPDF * normpdf(x, mu, sigma) + ~isPDF * normcdf(x, mu, sigma);
                plot(ax, x, y); title(ax, '5. 正态分布');
                setFormula('$$PDF: \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$', ...
                           '$$E[X] = \mu$$', '$$Var[X] = \sigma^2$$');
            case 6 % 均匀分布
                a = 0; b = 10; x = linspace(a, b, 1000);
                y = isPDF * unifpdf(x, a, b) + ~isPDF * unifcdf(x, a, b);
                plot(ax, x, y); title(ax, '6. 均匀分布');
                setFormula('$$PDF: \frac{1}{b-a}$$', '$$E[X] = \frac{a+b}{2}$$', '$$Var[X] = \frac{(b-a)^2}{12}$$');
            case 7 % 指数分布
                lambda = 1; x = linspace(0, 10, 1000);
                y = isPDF * exppdf(x, 1/lambda) + ~isPDF * expcdf(x, 1/lambda);
                plot(ax, x, y); title(ax, '7. 指数分布');
                setFormula('$$PDF: \lambda e^{-\lambda x}$$', '$$E[X] = 1/\lambda$$', '$$Var[X] = 1/\lambda^2$$');
            case 8 % 伽马分布
                k = 2; lambda = 1; x = linspace(0, 15, 1000);
                y = isPDF * gampdf(x, k, 1/lambda) + ~isPDF * gamcdf(x, k, 1/lambda);
                plot(ax, x, y); title(ax, '8. 伽马分布');
                setFormula('$$PDF: \frac{\lambda^\alpha x^{\alpha-1} e^{-\lambda x}}{\Gamma(\alpha)}$$', ...
                           '$$E[X] = \alpha/\lambda$$', '$$Var[X] = k/\lambda^2$$');
            case 9 % 贝塔分布
                alpha = 2; beta = 5; x = linspace(0, 1, 1000);
                y = isPDF * betapdf(x, alpha, beta) + ~isPDF * betacdf(x, alpha, beta);
                plot(ax, x, y); title(ax, '9. 贝塔分布');
                setFormula('$$PDF: \frac{1}{B(\alpha,\beta)}x^{\alpha-1}(1-x)^{\beta-1}$$', ...
                           '$$E[X] = \frac{\alpha}{\alpha+\beta}$$', ...
                           '$$Var[X] = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$$');
        end
    end

    function setFormula(pdf_str, ex_str, var_str)
        formula_pdf.String = pdf_str;
        formula_ex.String = ex_str;
        formula_var.String = var_str;
    end

        function calculateResult(~, ~)
        val = distMenu.Value;
        xval = str2double(xInput.String);
        if isnan(xval)
            resultText.String = '请输入合法的数值';
            return;
        end
        isPDF = strcmp(bg.SelectedObject.String, 'PDF');

        switch val
            case 1  % 二项分布
                n = 10; p = 0.5;
                result = isPDF * binopdf(xval, n, p) + ~isPDF * binocdf(xval, n, p);

            case 2  % 泊松分布
                lambda = 3;
                result = isPDF * poisspdf(xval, lambda) + ~isPDF * poisscdf(xval, lambda);

            case 3  % 超几何分布
                N = 50; K = 20; n = 10;
                result = isPDF * hygepdf(xval, N, K, n) + ~isPDF * hygecdf(xval, N, K, n);

            case 4  % 几何分布
                p = 0.3;
                result = isPDF * geopdf(xval - 1, p) + ~isPDF * geocdf(xval - 1, p);

            case 5  % 正态分布
                mu = 0; sigma = 1;
                result = isPDF * normpdf(xval, mu, sigma) + ~isPDF * normcdf(xval, mu, sigma);

            case 6  % 均匀分布
                a = 0; b = 10;
                result = isPDF * unifpdf(xval, a, b) + ~isPDF * unifcdf(xval, a, b);

            case 7  % 指数分布
                lambda = 1;
                result = isPDF * exppdf(xval, 1/lambda) + ~isPDF * expcdf(xval, 1/lambda);

            case 8  % 伽马分布
                k = 2; lambda = 1;
                result = isPDF * gampdf(xval, k, 1/lambda) + ~isPDF * gamcdf(xval, k, 1/lambda);

            case 9  % 贝塔分布
                a = 2; b = 5;
                result = isPDF * betapdf(xval, a, b) + ~isPDF * betacdf(xval, a, b);

            otherwise
                result = NaN;
        end

        resultText.String = sprintf('结果：%.5f', result);
    end


    function exportImage(~, ~)
        [file, path] = uiputfile('*.png');
        if ischar(file)
            saveas(f, fullfile(path, file));
        end
    end
end
