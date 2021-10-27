import streamlit as st
import requests
# from get_area import get_area
import pydeck as pdk
import rasterio
import numpy as np
import time
import pandas as pd
import altair as alt

def app():
    coordinates = {
        "llx" : 146.2170658,
        "lly" : -20.2191192,
        "urx" : 146.4817976,
        "ury" : -20.0690283,
    }

    st.sidebar.header("Parameters")



    for key, value in coordinates.items():
        coordinates[key] = st.sidebar.text_input(
            f"Coordinate for {key}", value
        )

    dates = ["1987-12-01T10:00:00.000Z","1988-03-01T10:00:00.000Z","1988-06-01T10:00:00.000Z","1988-09-01T10:00:00.000Z","1988-12-01T10:00:00.000Z","1989-03-01T10:00:00.000Z","1989-06-01T10:00:00.000Z","1989-09-01T10:00:00.000Z","1989-12-01T11:00:00.000Z","1990-03-01T11:00:00.000Z","1990-06-01T10:00:00.000Z","1990-09-01T10:00:00.000Z","1990-12-01T11:00:00.000Z","1991-03-01T11:00:00.000Z","1991-06-01T10:00:00.000Z","1991-09-01T10:00:00.000Z","1991-12-01T11:00:00.000Z","1992-03-01T10:00:00.000Z","1992-06-01T10:00:00.000Z","1992-09-01T10:00:00.000Z","1992-12-01T10:00:00.000Z","1993-03-01T10:00:00.000Z","1993-06-01T10:00:00.000Z","1993-09-01T10:00:00.000Z","1993-12-01T10:00:00.000Z","1994-03-01T10:00:00.000Z","1994-06-01T10:00:00.000Z","1994-09-01T10:00:00.000Z","1994-12-01T10:00:00.000Z","1995-03-01T10:00:00.000Z","1995-06-01T10:00:00.000Z","1995-09-01T10:00:00.000Z","1995-12-01T10:00:00.000Z","1996-03-01T10:00:00.000Z","1996-06-01T10:00:00.000Z","1996-09-01T10:00:00.000Z","1996-12-01T10:00:00.000Z","1997-03-01T10:00:00.000Z","1997-06-01T10:00:00.000Z","1997-09-01T10:00:00.000Z","1997-12-01T10:00:00.000Z","1998-03-01T10:00:00.000Z","1998-06-01T10:00:00.000Z","1998-09-01T10:00:00.000Z","1998-12-01T10:00:00.000Z","1999-03-01T10:00:00.000Z","1999-06-01T10:00:00.000Z","1999-09-01T10:00:00.000Z","1999-12-01T10:00:00.000Z","2000-03-01T10:00:00.000Z","2000-06-01T10:00:00.000Z","2000-09-01T10:00:00.000Z","2000-12-01T10:00:00.000Z","2001-03-01T10:00:00.000Z","2001-06-01T10:00:00.000Z","2001-09-01T10:00:00.000Z","2001-12-01T10:00:00.000Z","2002-03-01T10:00:00.000Z","2002-06-01T10:00:00.000Z","2002-09-01T10:00:00.000Z","2002-12-01T10:00:00.000Z","2003-03-01T10:00:00.000Z","2003-06-01T10:00:00.000Z","2003-09-01T10:00:00.000Z","2003-12-01T10:00:00.000Z","2004-03-01T10:00:00.000Z","2004-06-01T10:00:00.000Z","2004-09-01T10:00:00.000Z","2004-12-01T10:00:00.000Z","2005-03-01T10:00:00.000Z","2005-06-01T10:00:00.000Z","2005-09-01T10:00:00.000Z","2005-12-01T10:00:00.000Z","2006-03-01T10:00:00.000Z","2006-06-01T10:00:00.000Z","2006-09-01T10:00:00.000Z","2006-12-01T10:00:00.000Z","2007-03-01T10:00:00.000Z","2007-06-01T10:00:00.000Z","2007-09-01T10:00:00.000Z","2007-12-01T10:00:00.000Z","2008-03-01T10:00:00.000Z","2008-06-01T10:00:00.000Z","2008-09-01T10:00:00.000Z","2008-12-01T10:00:00.000Z","2009-03-01T10:00:00.000Z","2009-06-01T10:00:00.000Z","2009-09-01T10:00:00.000Z","2009-12-01T10:00:00.000Z","2010-03-01T10:00:00.000Z","2010-06-01T10:00:00.000Z","2010-09-01T10:00:00.000Z","2010-12-01T10:00:00.000Z","2011-03-01T10:00:00.000Z","2011-06-01T10:00:00.000Z","2011-09-01T10:00:00.000Z","2011-12-01T10:00:00.000Z","2012-03-01T10:00:00.000Z","2012-06-01T10:00:00.000Z","2012-09-01T10:00:00.000Z","2012-12-01T10:00:00.000Z","2013-03-01T10:00:00.000Z","2013-06-01T10:00:00.000Z","2013-09-01T10:00:00.000Z","2013-12-01T10:00:00.000Z","2014-03-01T10:00:00.000Z","2014-06-01T10:00:00.000Z","2014-09-01T10:00:00.000Z","2014-12-01T10:00:00.000Z","2015-03-01T10:00:00.000Z","2015-06-01T10:00:00.000Z","2015-09-01T10:00:00.000Z","2015-12-01T10:00:00.000Z","2016-03-01T10:00:00.000Z","2016-06-01T10:00:00.000Z","2016-09-01T10:00:00.000Z","2016-12-01T10:00:00.000Z","2017-03-01T10:00:00.000Z","2017-06-01T10:00:00.000Z","2017-09-01T10:00:00.000Z","2017-12-01T10:00:00.000Z","2018-03-01T10:00:00.000Z","2018-06-01T10:00:00.000Z","2018-09-01T10:00:00.000Z","2018-12-01T10:00:00.000Z","2019-03-01T10:00:00.000Z","2019-06-01T10:00:00.000Z","2019-09-01T10:00:00.000Z","2019-12-01T00:00:00.000Z","2020-03-01T00:00:00.000Z","2020-06-01T00:00:00.000Z","2020-09-01T00:00:00.000Z","2020-12-01T00:00:00.000Z","2021-03-01T00:00:00.000Z"]

    llx = coordinates["llx"]
    lly = coordinates["lly"]
    urx = coordinates["urx"]
    ury = coordinates["ury"]

    ll = [llx,lly]
    ul = [llx, ury]
    ur = [urx,ury]
    lr = [urx,lly]


    IMG_URL = 'https://geoserver.tern.org.au/geoserver/aus/wms?service=WMS&version=1.1.0&request=GetMap&layers=aus:fractional_cover&styles=&bbox=146.2170658,-20.2191192,146.4817976,-20.0690283&width=768&height=733&srs=EPSG:4326&format=image/vnd.jpeg-png8'
    urlp = 'https://geoserver.tern.org.au/geoserver/aus/wms?service=WMS&version=1.1.0&request=GetMap&layers=aus:ground_cover&styles=&bbox='
    urlbb = str(llx)+','+str(lly)+','+str(urx)+','+str(ury)
    urls = '&width=768&height=733&srs=EPSG:4326&format=image/vnd.jpeg-png8&time='

    # time ='2021-03-01T00:00:00.000Z'
    IMG_URL = urlp+urlbb+urls

    BOUNDS=[ll,ul,ur,lr]



    st.title("Birds eye view")
    st.header("Ground cover comparison")

    # TODO: Working shortening of date picker, just slow
    # DD=[]
    # for i in dates:
    #     DD.append(i[:7])

    # display = DD

    # options = list(range(len(dates)))

    # sdate = st.selectbox("", options, format_func=lambda x: display[x])
    # sdate = DD[sdate]+'-01T10:00:00.000Z'
    # st.write(sdate)


    col1, col2 = st.columns(2)

    with col1:
        sdate = st.selectbox(
            ' ',
            dates)

        # st.write('You selected:', sdate)
        # image 1
        bitmap_layer = pdk.Layer("BitmapLayer", image=IMG_URL+sdate, bounds=BOUNDS, opacity=0.7)
        view_state = pdk.ViewState(
            latitude=(float(lly)+float(ury))/2,
            longitude=(float(llx)+float(urx))/2,
            zoom=10,
            bearing=0,
            pitch=0,
            width="100%",
        )
        sr = pdk.Deck(bitmap_layer, initial_view_state=view_state, map_style=pdk.map_styles.ROAD)
        sr.to_html("bitmap_layer.html")
        st.write(sr)

    with col2:
        edate = st.selectbox(
        '  ',
        dates)
        # st.write('You selected:', edate)
        # image 2
        bitmap_layer = pdk.Layer("BitmapLayer", image=IMG_URL+edate, bounds=BOUNDS, opacity=0.7)
        view_state = pdk.ViewState(
            latitude=(float(lly)+float(ury))/2,
            longitude=(float(llx)+float(urx))/2,
            zoom=10,
            bearing=0,
            pitch=0,
            width="100%",
        )
        er = pdk.Deck(bitmap_layer, initial_view_state=view_state, map_style=pdk.map_styles.ROAD)
        er.to_html("bitmap_layer.html")
        st.write(er)
        


    ## Line graph ##
    dates2 = ["1987-12-01T10:00:00.000Z","1988-03-01T10:00:00.000Z","1988-06-01T10:00:00.000Z","1988-09-01T10:00:00.000Z","1988-12-01T10:00:00.000Z","1989-03-01T10:00:00.000Z","1989-06-01T10:00:00.000Z","1989-09-01T10:00:00.000Z","1989-12-01T11:00:00.000Z","1990-03-01T11:00:00.000Z","1990-06-01T10:00:00.000Z","1990-09-01T10:00:00.000Z","1990-12-01T11:00:00.000Z","1991-03-01T11:00:00.000Z","1991-06-01T10:00:00.000Z","1991-09-01T10:00:00.000Z","1991-12-01T11:00:00.000Z","1992-03-01T10:00:00.000Z","1992-06-01T10:00:00.000Z","1992-09-01T10:00:00.000Z","1992-12-01T10:00:00.000Z","1993-03-01T10:00:00.000Z","1993-06-01T10:00:00.000Z","1993-09-01T10:00:00.000Z","1993-12-01T10:00:00.000Z","1994-03-01T10:00:00.000Z","1994-06-01T10:00:00.000Z","1994-09-01T10:00:00.000Z","1994-12-01T10:00:00.000Z","1995-03-01T10:00:00.000Z","1995-06-01T10:00:00.000Z","1995-09-01T10:00:00.000Z","1995-12-01T10:00:00.000Z","1996-03-01T10:00:00.000Z","1996-06-01T10:00:00.000Z","1996-09-01T10:00:00.000Z","1996-12-01T10:00:00.000Z","1997-03-01T10:00:00.000Z","1997-06-01T10:00:00.000Z","1997-09-01T10:00:00.000Z","1997-12-01T10:00:00.000Z","1998-03-01T10:00:00.000Z","1998-06-01T10:00:00.000Z","1998-09-01T10:00:00.000Z","1998-12-01T10:00:00.000Z","1999-03-01T10:00:00.000Z","1999-06-01T10:00:00.000Z","1999-09-01T10:00:00.000Z","1999-12-01T10:00:00.000Z","2000-03-01T10:00:00.000Z","2000-06-01T10:00:00.000Z","2000-09-01T10:00:00.000Z","2000-12-01T10:00:00.000Z","2001-03-01T10:00:00.000Z","2001-06-01T10:00:00.000Z","2001-09-01T10:00:00.000Z","2001-12-01T10:00:00.000Z","2002-03-01T10:00:00.000Z","2002-06-01T10:00:00.000Z","2002-09-01T10:00:00.000Z","2002-12-01T10:00:00.000Z","2003-03-01T10:00:00.000Z","2003-06-01T10:00:00.000Z","2003-09-01T10:00:00.000Z","2003-12-01T10:00:00.000Z","2004-03-01T10:00:00.000Z","2004-06-01T10:00:00.000Z","2004-09-01T10:00:00.000Z","2004-12-01T10:00:00.000Z","2005-03-01T10:00:00.000Z","2005-06-01T10:00:00.000Z","2005-09-01T10:00:00.000Z","2005-12-01T10:00:00.000Z","2006-03-01T10:00:00.000Z","2006-06-01T10:00:00.000Z","2006-09-01T10:00:00.000Z","2006-12-01T10:00:00.000Z","2007-03-01T10:00:00.000Z","2007-06-01T10:00:00.000Z","2007-09-01T10:00:00.000Z","2007-12-01T10:00:00.000Z","2008-03-01T10:00:00.000Z","2008-06-01T10:00:00.000Z","2008-09-01T10:00:00.000Z","2008-12-01T10:00:00.000Z","2009-03-01T10:00:00.000Z","2009-06-01T10:00:00.000Z","2009-09-01T10:00:00.000Z","2009-12-01T10:00:00.000Z","2010-03-01T10:00:00.000Z","2010-06-01T10:00:00.000Z","2010-09-01T10:00:00.000Z","2010-12-01T10:00:00.000Z","2011-03-01T10:00:00.000Z","2011-06-01T10:00:00.000Z","2011-09-01T10:00:00.000Z","2011-12-01T10:00:00.000Z","2012-03-01T10:00:00.000Z","2012-06-01T10:00:00.000Z","2012-09-01T10:00:00.000Z","2012-12-01T10:00:00.000Z","2013-03-01T10:00:00.000Z","2013-06-01T10:00:00.000Z","2013-09-01T10:00:00.000Z","2013-12-01T10:00:00.000Z","2014-03-01T10:00:00.000Z","2014-06-01T10:00:00.000Z","2014-09-01T10:00:00.000Z","2014-12-01T10:00:00.000Z","2015-03-01T10:00:00.000Z","2015-06-01T10:00:00.000Z","2015-09-01T10:00:00.000Z","2015-12-01T10:00:00.000Z","2016-03-01T10:00:00.000Z","2016-06-01T10:00:00.000Z","2016-09-01T10:00:00.000Z","2016-12-01T10:00:00.000Z","2017-03-01T10:00:00.000Z","2017-06-01T10:00:00.000Z","2017-09-01T10:00:00.000Z","2017-12-01T10:00:00.000Z","2018-03-01T10:00:00.000Z","2018-06-01T10:00:00.000Z","2018-09-01T10:00:00.000Z","2018-12-01T10:00:00.000Z","2019-03-01T10:00:00.000Z","2019-06-01T10:00:00.000Z","2019-09-01T10:00:00.000Z","2019-12-01T00:00:00.000Z","2020-03-01T00:00:00.000Z","2020-06-01T00:00:00.000Z","2020-09-01T00:00:00.000Z","2020-12-01T00:00:00.000Z","2021-03-01T00:00:00.000Z"]


    urls2 = '&width=768&height=733&srs=EPSG:4326&format=image/tiff&time='
    IMG_URL2 = urlp+urlbb+urls2
    Dates = []
    GC1 = []
    GC2 = []
    GC3 = []

    s=time.time() # REMOVE
    for i in dates2[115:]: # TODO: add in variable date [125:] is good
        file=IMG_URL2+i
        with rasterio.open(file) as src:
            Dates.append(i[:7])

            GC1a=src.read(1).astype('float')
            GC1a[GC1a==0]=np.nan
            GC1a=np.nanmean(GC1a)
            GC1.append(GC1a)

            GC2a=src.read(2).astype('float')
            GC2a[GC2a==0]=np.nan
            GC2a=np.nanmean(GC2a)
            GC2.append(GC2a)

            GC3a=src.read(3).astype('float')
            GC3a[GC3a==0]=np.nan
            GC3a=np.nanmean(GC3a)
            GC3.append(GC3a)

            # GC1.append(np.nanmean(src.read(1))) # change for diff bands
            # GC2.append(np.nanmean(src.read(2))) # change for diff bands
            # GC3.append(np.nanmean(src.read(3))) # change for diff bands

    e=time.time() # REMOVE
    print(e-s) # REMOVE



    df = pd.DataFrame({
        'x':Dates,
        'Bare ground':GC1,
        'Green vegetation':GC2,
        'Non-green vegetation':GC3,
        })

 

    # st.line_chart(df.set_index('x'),use_container_width=True) # plain st line 


    # ==============================

    source=df.melt('x', var_name='category', value_name='y')

    # Create a selection that chooses the nearest point & selects based on x-value
    nearest = alt.selection(type='single', nearest=True, on='mouseover',
                            fields=['x'], empty='none')

    # The basic line
    domain = ['Bare ground','Green vegetation','Non-green vegetation']
    range_ = ['red','green','blue']

    line = alt.Chart(source).mark_line(interpolate='basis').encode(
        x='x',
        y='y',
        color=alt.Color('category', scale=alt.Scale(domain=domain,range=range_)
    ))

    # Transparent selectors across the chart. This is what tells us
    # the x-value of the cursor
    selectors = alt.Chart(source).mark_point().encode(
        x='x',
        opacity=alt.value(0),
    ).add_selection(
        nearest
    )

    # Draw points on the line, and highlight based on selection
    points = line.mark_point().encode(
        opacity=alt.condition(nearest, alt.value(1), alt.value(0))
    )

    # Draw text labels near the points, and highlight based on selection
    text = line.mark_text(align='left', dx=5, dy=-5).encode(
        text=alt.condition(nearest, 'y', alt.value(' '))
    )

    # Draw a rule at the location of the selection
    rules = alt.Chart(source).mark_rule(color='gray').encode(
        x='x',
    ).transform_filter(
        nearest
    )

    # Put the five layers into a chart and bind the data
    chart=alt.layer(
        line, selectors, points, rules, text
    ).properties(
        width=600, height=300
    )
    st.altair_chart(chart, use_container_width=True)
    # ==============================


    st.write(df)
    st.write(IMG_URL)
    # st.text("band 1 - bare ground fraction (in percent) + 100")
    # st.text("band 2 - green vegetation fraction (in percent) +100")
    # st.text("band 3 - non-green vegetation fraction (in percent) + 100")


    # Layers=[
    #     pdk.Layer("BitmapLayer", image=IMG_URL+sdate, 
    #     bounds=[
    #             [llx,lly],
    #             [llx,ury],
    #             [(float(urx)+float(llx))/2,ury],
    #             [(float(urx)+float(llx))/2,lly],
    #             ], 
    #     opacity=0.7,
    #     extruded=False,
    #     coverage=1),
    #     pdk.Layer("BitmapLayer", image=IMG_URL+edate, 
    #     bounds= [
    #             [((float(urx)-float(llx))*.5)+float(llx),lly],
    #             [((float(urx)-float(llx))*.5)+float(llx),ury],
    #             ur,
    #             lr,
    #             ], 
    #     opacity=0.7,
    #     extruded=False,
    #     coverage=1),
    #         ]
    # view_state = pdk.ViewState(
    #     latitude=(float(lly)+float(ury))/2,
    #     longitude=(float(llx)+float(urx))/2,
    #     zoom=10,
    #     bearing=0,
    #     pitch=0,
    #     width='100%',
    # )
    # er = pdk.Deck(Layers, initial_view_state=view_state, map_style=pdk.map_styles.ROAD)
    # er.to_html("bitmap_layer.html")
    # st.write(er)




    # # TESTING
    # st.write(BOUNDS)
    # st.write(BOUNDS[2][0])
    # st.write(BOUNDS[3][0])

    # BOUNDS=[ll,ul,ur,lr]

    # BOUNDS = [
    # [llx,lly]
    # [llx,ury]
    # [urx*.5,ury]
    # [urx*.5,lly]
    # ]



    # surlbb = str(llx)+','+str(lly)+','+str(urx)+','+str(ury)
    # eurlbb = str(llx)+','+str(lly)+','+str(urx)+','+str(ury)
    # test = ((float(urx)-float(llx))*.5)+float(llx)


    st.write(IMG_URL+sdate)
    st.write(IMG_URL+edate)