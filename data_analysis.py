import numpy as np
import pandas as pd




if __name__ == '__main__' :
    st.title("SCADA数据分析")
    # ---------------------------主栏-----------------------
    # ---------------------------读入数据-----------------------
    st.write("")
    st.write("")
    st.header('------------------------数据读入------------------------')  # 设置主栏第一部分
    st.sidebar.header('-----------------数据读入-----------------')  # 设置设置侧栏第一部分
    st.sidebar.subheader('* 数据上传 *')
    st.subheader('* 数据说明 *')
    file = st.sidebar.file_uploader('上传数据', type=['csv'], key=None)
    scada_data = pd.read_csv(file)
    # df = get_data(file)
    st.dataframe(scada_data)
    st.sidebar.subheader('* 时间序列 *')
    st.subheader('* 时间序列 *')
    options = np.array(scada_data['real_time']).tolist()
    (start_time, end_time) = st.select_slider("请选择时间序列：", options=options,
                                              value=(options[0], options[len(options) - 1]))
    # setting index as date
    scada_data['real_time'] = pd.to_datetime(scada_data['real_time'], format='%Y-%m-%d')
    scada_data.index = scada_data['real_time']
    st.write("序列开始时间：", start_time)
    st.write("序列结束时间：", end_time)
    scada_data = scada_data[start_time:end_time]
    st.dataframe(scada_data)
  



